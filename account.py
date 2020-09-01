import json
import os

import tools
from db_config import *

class Account:
	@staticmethod
	def get():
		"""Returns all existing accounts list
		:return: list
		"""
		with open(DB_JSON_ACCOUNTS_PATH, "rt") as jfl:
			data = json.load(jfl)

		return list(data) # list(data.keys())

	@staticmethod
	def create(login, password=""):
		"""Creates an account in the database
		:param login: str
		:param password: str
		"""
		with open(DB_JSON_ACCOUNTS_PATH, "rt") as jfl:
			accounts = json.load(jfl)

		# add new account
		if not login in accounts:
			accounts[login] = password
			tools.success(f"the {login} account was created successfully")
		else:
			tools.error("already have this account")
			return

		# save new data
		with open(DB_JSON_ACCOUNTS_PATH, "wt") as jfl:
			json.dump(accounts, jfl, sort_keys=True, indent=4)

	@staticmethod
	def remove(login):
		"""Removes an account from the database
		:param login: str
		"""
		# guest account can not be removed
		if login == "guest":
			tools.error("guest account can not be removed")
			return

		with open(DB_JSON_ACCOUNTS_PATH, "rt") as jfl:
			accounts = json.load(jfl)

		# removing the account from the database.
		# dict.pop returns the value of just
		# removed key. so if dict.pop returns
		# None it means that no such account was
		# in the database at all
		if accounts.pop(login, None) is None:
			tools.warn(f"no such account '{login}'")
			return

		# new data
		with open(DB_JSON_ACCOUNTS_PATH, "wt") as jfl:
			json.dump(accounts, jfl, sort_keys=True, indent=4)

		tools.warn(f"account '{login}' has been just removed")

	@staticmethod
	def get_password_by_login(login):
		"""Returns a password of the account with such login
		:param login: str
		:return: str
		"""
		# get data
		with open(DB_JSON_ACCOUNTS_PATH, "rt") as jfl:
			data = json.load(jfl)

		return data.get(login)
