import json
import os

import tools
from db_config import *

class Task:
	@staticmethod
	def remove_accounts_tasks(account):
		"""Removes all tasks of an account
		:account: str
		"""
		with open(DB_JSON_TASKS_PATH, "rt") as jfl:
			data = json.load(jfl)

		if account != "guest":
			data.pop(account, None)
			tools.warn(f"all tasks of '{account}' account were removed")

		# save new data
		with open(DB_JSON_TASKS_PATH, "wt") as jfl:
			json.dump(data, jfl, sort_keys=True, indent=4)

	@staticmethod
	def get(account="guest"):
		"""Returns all account's tasks from the database
		Returns a dict where the key is task itself and the
		value is status of the task.
		:param account: str
		:return: dict
		"""
		with open(DB_JSON_TASKS_PATH, "rt") as jfl:
			data = json.load(jfl)

		return data.get(account)

	@staticmethod
	def create(task, account="guest"):
		"""Creates a task (adds to a tasklist)
		:param task: str
		:param account: str
		"""
		# loading the data
		with open(DB_JSON_TASKS_PATH, "rt") as jfl:
			tasks = json.load(jfl)

		if task in tasks[account]:
			tools.error("already have this task in tasklist")
			return

		tasks[account][task] = False # key is task, value is status

		# save new data
		with open(DB_JSON_TASKS_PATH, "wt") as jfl:
			json.dump(tasks, jfl, sort_keys=True, indent=4)

	@staticmethod
	def create_slot_for(account):
		"""Creates account: {} in tasks.json
		:param account: str
		"""
		with open(DB_JSON_TASKS_PATH, "rt") as jfl:
			tasks = json.load(jfl)

		tasks[account] = {}

		# save new data
		with open(DB_JSON_TASKS_PATH, "wt") as jfl:
			json.dump(tasks, jfl, sort_keys=True, indent=4)

	@staticmethod
	def remove(task, account="guest"):
		# loading the data
		with open(DB_JSON_TASKS_PATH, "rt") as jfl:
			tasks = json.load(jfl)

		if task in tasks[account]:
			del tasks[account][task]
			tools.warn(f"task '{task}' was removed")
		else:
			tools.error("no such task")

		# load/save new data
		with open(DB_JSON_TASKS_PATH, "wt") as jfl:
			json.dump(tasks, jfl, sort_keys=True, indent=4)

	@staticmethod
	def mark_as(task, account="guest", done=False):
		"""Marks a task as done or in-progress
		:param task: str
		:param account: str
		"""
		with open(DB_JSON_TASKS_PATH, "rt") as jfl:
			tasks = json.load(jfl)

		if task in tasks[account]:
			tasks[account][task] = done
		else:
			tools.error("no such task")

		# save new data
		with open(DB_JSON_TASKS_PATH, "wt") as jfl:
			json.dump(tasks, jfl, sort_keys=True, indent=4)

		