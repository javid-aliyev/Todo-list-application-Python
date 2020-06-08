"""Tasks CRUD"""

from database import Database
import decorators
from sqlite3 import IntegrityError
import colorama

colorama.init()

class Tasks:
	@staticmethod
	def get():
		"""Returns a list of tasks
		:return: list
		"""
		with Database() as cursor:
			executed = cursor.execute("SELECT * FROM tasks")
			tasks = [i[1] for i in executed]
		return tasks

	@staticmethod
	def print():
		"""Prints all tasks. Done tasks marked green"""
		tasks = Tasks.get()
		for index, task in enumerate(tasks, 1):
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
				try:
					cursor.execute(f"INSERT INTO tasks ('task', 'is_done') VALUES ('{task}', 0)")
					print(f"task '{task}' was successfully created!")
				except IntegrityError:
					print("task must be unique")
					return

	@staticmethod
	@decorators.red_output
	def delete(task):
		"""Removes a task if the task is in database
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
			cursor.execute("DELETE FROM tasks")
			print(f"all tasks were successfully removed")

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
	def undone(task):
		"""Notes in the database that the task has not been completed"""
		tasks = Tasks.get()
		with Database() as cursor:
			if task in tasks:
				cursor.execute(f"UPDATE tasks SET is_done = 0 WHERE task = '{task}'")
				print(f"the task {task} was marked in-progress")

	@staticmethod
	def is_done(task):
		"""If the task is done then it returns True
		:param task: str
		:return: bool
		"""
		tasks = Tasks.get()
		with Database() as cursor:
			if task in tasks:
				result = cursor.execute(f"SELECT * FROM tasks WHERE task = '{task}'").fetchone()
				return bool(result[2]) # result[2] is is_done column
