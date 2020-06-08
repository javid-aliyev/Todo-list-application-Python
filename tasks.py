"""Tasks CRUD"""

from database import Database
from sqlite3 import IntegrityError
import decorators

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
	@decorators.green_output
	def print():
		"""Prints all tasks"""
		tasks = Tasks.get()
		for index, task in enumerate(tasks, 1):
			print(f"{index}. {task}")

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
	def delete(task):
		"""Removes a task if the task is in database
		:param task: str
		"""
		tasks = Tasks.get()
		with Database() as cursor:
			if task in tasks:
				cursor.execute(f"DELETE FROM tasks WHERE task = '{task}'")
				print(f"'{task}' was successfully removed")
			else:
				print("no such task")
				return

	@staticmethod
	def delete_tasks():
		"""Removes all tasks"""
		with Database() as cursor:
			cursor.execute("DELETE FROM tasks")
			print(f"all tasks were successfully removed")

	@staticmethod
	def done(task):
		"""Notes in the database that the task has been completed
		:param task: str
		:return: None"""
		tasks = Tasks.get()
		with Database() as cursor:
			if task in tasks:
				cursor.execute(f"UPDATE tasks SET is_done = 1 WHERE task = '{task}'")
				print(f"the task {task} was marked completed")
			else:
				print("no such task")
				return

	@staticmethod
	def is_done(task):
		"""If the task is done then it returns True
		:param task: str
		:return: bool
		"""

		"""REWRITE!"""
		tasks = Tasks.get()
		with Database() as cursor:
			if task in tasks:
				result = cursor.execute(f"SELECT is_done FROM tasks WHERE task = '{task}'").fetchall()
				return result

# print(Tasks.is_done("go to the doctor"))
