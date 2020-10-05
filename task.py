import os

import tools
from config import *

class Task:
	@staticmethod
	def remove_accounts_tasks(account):
		"""Removes all tasks of an account (and its "slot")
		:account: str
		"""
		data = tools.get_json_from_file(TASKS_JSON)

		if account != "guest":
			data.pop(account, None)
			tools.warn(f"all tasks of '{account}' account were removed (and slot)")

		tools.save_json_to_file(TASKS_JSON, data)

	@staticmethod
	def remove_accounts_tasks_without_slot(account):
		"""Removes all tasks of an account (but stores its slot)
		:account: str
		"""
		data = tools.get_json_from_file(TASKS_JSON)

		data[account] = {}
		tools.warn(f"all tasks of '{account}' account were removed")

		tools.save_json_to_file(TASKS_JSON, data)

	@staticmethod
	def get(account="guest"):
		"""Returns all account's tasks from the database
		Returns a dict where the key is task itself and the
		value is status of the task.
		:param account: str
		:return: dict
		"""
		data = tools.get_json_from_file(TASKS_JSON)

		return data.get(account)

	@staticmethod
	def create(task, account="guest"):
		"""Creates a task (adds to a tasklist)
		:param task: str
		:param account: str
		"""
		tasks = tools.get_json_from_file(TASKS_JSON)

		if task in tasks[account]:
			tools.error("already have this task in tasklist")
			return

		tasks[account][task] = False # key is task, value is status

		tools.save_json_to_file(TASKS_JSON, tasks)

	@staticmethod
	def create_slot_for(account):
		"""Creates account: {} in tasks.json
		:param account: str
		"""
		tasks = tools.get_json_from_file(TASKS_JSON)

		tasks[account] = {}

		tools.save_json_to_file(TASKS_JSON, tasks)

	@staticmethod
	def remove(task, account="guest"):
		tasks = tools.get_json_from_file(TASKS_JSON)

		if task in tasks[account]:
			del tasks[account][task]
			tools.warn(f"task '{task}' was removed")
		else:
			tools.error("no such task")

		tools.save_json_to_file(TASKS_JSON, tasks)

	@staticmethod
	def mark_as(task, account="guest", done=False):
		"""Marks a task as done or in-progress
		:param task: str
		:param account: str
		"""
		tasks = tools.get_json_from_file(TASKS_JSON)


		if task in tasks[account]:
			tasks[account][task] = done
		else:
			tools.error("no such task")

		tools.save_json_to_file(TASKS_JSON, tasks)

		
