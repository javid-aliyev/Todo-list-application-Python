import os

import tools
from db_config import *

class Account:
	@staticmethod
	def get():
		"""Returns all existing accounts list
		:return: list
		"""
		data = tools.get_json_from_file(DB_JSON_ACCOUNTS_PATH)

		return list(data) # list(data.keys())

	@staticmethod
	def create(login, password=""):
		"""Creates an account in the database
		Password would be hashed
		:param login: str
		:param password: str
		"""
		accounts = tools.get_json_from_file(DB_JSON_ACCOUNTS_PATH)

		# add new account
		if not login in accounts:
			accounts[login] = password
			tools.success(f"the {login} account was created successfully")
		else:
			tools.error("already have this account")
			return

		tools.save_json_to_file(DB_JSON_ACCOUNTS_PATH, accounts)

	@staticmethod
	def remove(login):
		"""Removes an account from the database
		:param login: str
		"""
		# guest account can not be removed
		if login == "guest":
			tools.error("guest account can not be removed")
			return

		accounts = tools.get_json_from_file(DB_JSON_ACCOUNTS_PATH)

		# removing the account from the database.
		# dict.pop returns the value of just
		# removed key. so if dict.pop returns
		# None it means that no such account was
		# in the database at all
		if accounts.pop(login, None) is None:
			tools.warn(f"no such account '{login}'")
			return

		tools.save_json_to_file(DB_JSON_ACCOUNTS_PATH, accounts)

		tools.warn(f"account '{login}' has been just removed")

	@staticmethod
	def get_password_by_login(login):
		"""Returns a (hashed) password of the account with such login
		:param login: str
		:return: str
		"""
		data = tools.get_json_from_file(DB_JSON_ACCOUNTS_PATH)

		return data.get(login)
