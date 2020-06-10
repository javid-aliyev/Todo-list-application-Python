"""Tasks CRUD"""

from database import Database
import decorators
from accounts import Accounts

from sqlite3 import IntegrityError
import colorama

colorama.init()

class Tasks:
	@staticmethod
	def get():
		"""Returns a list of tasks of account
		:return: list
		"""
		with Database() as cursor:
			executed = cursor.execute(
				f"SELECT * FROM tasks WHERE account_id = {Accounts.account_id}"
			)
			tasks = [i[1] for i in executed]
		return tasks

	@staticmethod
	def print():
		"""Prints all tasks of the account. Done tasks marked green"""
		tasks = Tasks.get()
		for index, task in enumerate(tasks, 1):
			if Tasks.belongs_to_account(task):
				if Tasks.is_done(task):
					print(f"{colorama.Fore.BLUE}{index}.{colorama.Style.RESET_ALL} {colorama.Fore.GREEN}{task}{colorama.Style.RESET_ALL}")
				else:
					print(f"{colorama.Fore.BLUE}{index}.{colorama.Style.RESET_ALL} {task}")

	@staticmethod
	@decorators.green_output
	def add(task):
		"""Adds a new task to the database.
		:param task: string
		"""
		with Database() as cursor:
			if task:
				if not '\'' in task:
					try:
						cursor.execute(
							f"INSERT INTO tasks ('task', 'is_done', 'account_id') VALUES ('{task}', 0, {Accounts.account_id})"
						)
						print(f"task '{task}' was successfully created!")
					except IntegrityError:
						print("task must be unique. maybe any other account has same task")
				else:
					print("there must be no ' char in task")

	@staticmethod
	@decorators.red_output
	def delete(task):
		"""Removes a task if the task belongs to the current user
		:param task: str
		"""
		tasks = Tasks.get()
		with Database() as cursor:
			if task in tasks:
				cursor.execute(f"DELETE FROM tasks WHERE task = '{task}'")
				print(f"'{task}' was successfully removed")

	@staticmethod
	@decorators.red_output
	def delete_tasks():
		"""Removes all tasks"""
		with Database() as cursor:
			cursor.execute(f"DELETE FROM tasks WHERE account_id = '{Accounts.account_id}'")
			print(f"all {Accounts.account}'s tasks were successfully removed")

	@staticmethod
	@decorators.green_output
	def done(task):
		"""Notes in the database that the task has been completed
		:param task: str
		:return: None"""
		tasks = Tasks.get()
		with Database() as cursor:
			if task in tasks:
				cursor.execute(f"UPDATE tasks SET is_done = 1 WHERE task = '{task}'")
				print(f"the task {task} was marked completed")

	@staticmethod
	@decorators.green_output
	def undone(task):
		"""Notes in the database that the task has not been completed"""
		tasks = Tasks.get()
		with Database() as cursor:
			if task in tasks:
				cursor.execute(f"UPDATE tasks SET is_done = 0 WHERE task = '{task}'")
				print(f"the task {task} was marked in-progress")

	@staticmethod
	def is_done(task):
		"""If the task is done then it returns True otherwise False
		:param task: str
		:return: bool
		"""
		tasks = Tasks.get()
		with Database() as cursor:
			if task in tasks:
				result = cursor.execute(
					f"SELECT * FROM tasks WHERE task = '{task}'"
				).fetchone()
				return bool(result[2]) # result[2] is is_done column

	@staticmethod
	def belongs_to_account(task):
		"""Checks if the task belongs to the account(account_id)
		:param task: str
		:return: bool
		"""
		tasks = Tasks.get()
		return task in tasks

