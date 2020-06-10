"""Main module"""

import sys

import utils
from tasks import Tasks
from accounts import Accounts

class Program:
	def __init__(self):
		self.commands = ["add", "ls", "rm", "rmall", "done",
						"undone", ":whoami", ":addacc", ":rmacc",
						":lsaccs", ":login", ":quit", ":clear",
						":help"]
		self.curr_account = Accounts.get_username_by_id(Accounts.account_id)
		self.main()

	def execute_command(self, command):
		"""Executes the command"""
		if command == "add":
			task = utils.sinput("task: ")
			Tasks.add(task)
		elif command == "ls":
			Tasks.print()
		elif command == "rm":
			task = utils.sinput("task: ")
			Tasks.delete(task)
		elif command == "rmall":
			Tasks.delete_tasks()
		elif command == "done":
			task = utils.sinput("task: ")
			Tasks.done(task)
		elif command == "undone":
			task = utils.sinput("task: ")
			Tasks.undone(task)
		elif command == ":quit":
			sys.exit()
		elif command == ":clear":
			utils.clear_console()
		elif command == ":help":
			utils.print_help_info(self.commands)
		elif command == ":whoami":
			# print(self.curr_account)
			Accounts.whoami()
		elif command == ":addacc":
			new_account_username = utils.sinput("username? ")
			new_account_password = utils.secured_sinput("password? ")
			Accounts.add(new_account_username, new_account_password)
		elif command == ":rmacc":
			account_to_delete = utils.sinput("username of an account to delete? ")
			npt_password_of_account_to_delete = utils.secured_sinput("password? ")
			real_password_of_account_to_delete = Accounts.get_password_by_username(account_to_delete)
			# if user is not deleting account which is curr_account and
			# if inputted password = to real password of this account
			if account_to_delete != self.curr_account and \
				npt_password_of_account_to_delete == real_password_of_account_to_delete:
				Accounts.delete(account_to_delete)
		elif command == ":lsaccs":
			Accounts.print()
		elif command == ":login":
			account_to_login = utils.sinput("username: ")
			npt_password_of_account_to_login = utils.secured_sinput("password: ")
			real_password_of_account_to_login = Accounts.get_password_by_username(account_to_login)
			if npt_password_of_account_to_login == real_password_of_account_to_login:
				Accounts.authorize(account_to_login)
		elif command == "":
			return
		else:
			print("no such command")

	def main(self):
		while True:
			self.curr_account = Accounts.get_username_by_id(Accounts.account_id)
			command = utils.sinput("# ")
			self.execute_command(command)

if __name__ == "__main__":
	Program()