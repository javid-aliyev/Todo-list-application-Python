"""
CRUD for accounts
"""

from database import Database
import decorators

from sqlite3 import IntegrityError

class Accounts:
	account_id = 1 # guest | curr_account_id

	@staticmethod
	def get():
		"""Returns all accounts from the database
		:return: list
		"""
		with Database() as cursor:
			executed = cursor.execute("SELECT * FROM accounts")
			accounts = [i[1] for i in executed] # usernames
		return accounts

	@staticmethod
	def get_id_by_username(username):
		"""Returns id of account by username from accounts table
		:param username: str
		:return: int
		"""
		with Database() as cursor:
			account_id = cursor.execute(
				f"SELECT * FROM accounts WHERE username = '{username}'"
			).fetchone()
			return account_id[0]

	@staticmethod
	def get_username_by_id(account_id):
		"""Returns username of account by account's id
		:param account_id: int
		:return: str
		"""
		with Database() as cursor:
			return cursor.execute(
				f"SELECT * FROM accounts WHERE id = {account_id}"
			).fetchone()[1] # [1] is username

	@staticmethod
	def get_password_by_id(account_id):
		"""Returns password of account with account_id id
		:param account_id: int
		:return: str
		"""
		with Database() as cursor:
			return cursor.execute(
				f"SELECT * FROM accounts WHERE id = {account_id}"
			).fetchone()[2] # [2] is password

	@staticmethod
	def get_password_by_username(username):
		with Database() as cursor:
			try:
				return cursor.execute(
					f"SELECT * FROM accounts WHERE username = '{username}'"
				).fetchone()[2]
			except TypeError:
				return

	@staticmethod
	@decorators.blue_output
	def print():
		"""Prints all accounts in the database"""
		accounts = Accounts.get()
		for account in accounts:
			print(f"~ {account}")

	@staticmethod
	def add(username, password):
		"""Adds a new account to the database
		:param username: str
		:param password: str
		"""
		if username and password:	
			with Database() as cursor:
				try:
					cursor.execute(
						f"INSERT INTO accounts ('username', 'password') VALUES ('{username}', '{password}')"
					)
				except IntegrityError:
					print("already have an account with that username")

	@staticmethod
	@decorators.red_output
	def delete(username):
		"""Deletes given account
		:param account: str
		"""
		if username:
			with Database() as cursor:
				cursor.execute(
					f"DELETE FROM accounts WHERE username = '{username}'"
				)
				print(f"the '{username}' account was successfully removed")

	@staticmethod
	def authorize(username):
		"""Authorizes user. Changes Tasks account_id.
		username is account to login
		:param username: str
		"""
		Accounts.account_id = Accounts.get_id_by_username(username)
		print(f"logged in as {Accounts.get_username_by_id(Accounts.account_id)}")

	@staticmethod
	@decorators.green_output
	def whoami():
		print(Accounts.get_username_by_id(Accounts.account_id))