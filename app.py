import sys

import tools
from task import Task
from account import Account

class App:
	def __init__(self, argv):
		self._argv = argv
		self.id2task = {} # tools._id2task
		self.account = "guest" # current account
		self.main()

	def _execute_command(self, command):
		"""Executes a given command (account param is current active account)
		:param command: str
		:param account: str
		"""
		# task
		if command == "add":
			task = tools._sinput("task? ").strip()
			if task != "":
				Task.create(task, self.account)
		elif command == "rm": # add index feature
			task = tools._sinput("task to remove? ").strip()
			if task != "":
				Task.remove(task, self.account)
		elif command == "rmall":
			Task.remove_accounts_tasks(self.account)
		elif command == "ls":
			tasks = Task.get(self.account)
			if tasks:
				for task in tasks.items():
					if task[1]:
						tools.success(f"* {task[0]}") # green output print
					else:
						print(f"* {task[0]}")
		elif command == "done":
			task = tools._sinput("task? ")
			Task.mark_as(task, self.account, done=True)
		elif command == "undone":
			task = tools._sinput("task? ")
			Task.mark_as(task, self.account, done=False)

		# account
		elif command == "addacc":
			login = tools._sinput("login? ")
			password = tools._secured_sinput("password(not required)? ")
			if login.strip() == "":
				tools.warn("login form is required")
			else:
				Account.create(login, password)
				# a slot in tasks.json
				Task.create_slot_for(login)
		elif command == "rmacc":
			account = tools._sinput("account to remove? ")
			password = tools._secured_sinput("password of the account? ")
			real_password = Account.get_password_by_login(account)

			if account == "":
				tools.error("invalid account")
				return
			if account == self.account:
				tools.error("you cannot delete the account you are on at the moment (go to the guest account)")
				return
			if password == real_password:
				Account.remove(account)
				Task.remove_accounts_tasks(account)
		elif command == "lsaccs":
			for account in Account.get():
				if account == self.account:
					tools.success(f"* {account}")
				else:
					print(f"* {account}")
		elif command == "login":
			account = tools._sinput("account to login? ")
			password = tools._secured_sinput("password of the account? ")
			real_password = Account.get_password_by_login(account)
			if account == "":
				tools.error("invalid login")
				return
			if password == real_password and \
				(account in Account.get()):
				self.account = account
				tools.success(f"you logged in as {account}")
			else:
				tools.error("invalid login or password")
		elif command == "whoami":
			tools.success(self.account)

		# other commands
		elif command == ":quit":
			sys.exit()
		elif command == ":clear":
			tools._clear_console()
		elif command == ":help":
			tools._print_help_info()
		elif command == "":
			pass
		else:
			tools.error(f"no such command: '{command}'")

	def main(self):
		while True:
			npt = tools._sinput("~> ").strip()
			self._execute_command(npt)

if __name__ == "__main__":
	App(sys.argv)