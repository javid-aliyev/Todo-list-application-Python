"""Some utils for project"""

import platform
import os
import getpass
import sys

from decorators import *

commands = [
	"add",
	"ls",
	"rm",
	"rmall",
	"done",
	"undone",
	"whoami",
	"addacc",
	"rmacc",
	"lsaccs",
	"login",
	":quit",
	":clear",
	":help"
]

def _sinput(ps="~> "):
	"""Smart Input handles errors"""
	try:
		npt = input(ps).strip()
		return npt
	except (KeyboardInterrupt, EOFError):
		sys.exit()

def _secured_sinput(ps="~> "):
	try:
		npt = getpass.getpass(ps).strip()
		return npt
	except (KeyboardInterrupt, EOFError):
		sys.exit()

if platform.system().lower() == "windows":
	def _clear_console():
		"""Clears the console"""
		os.system("cls")
else:
	def _clear_console():
		"""Clears the console"""
		os.system("clear")

def _print_help_info():
	"""Prints help pages"""
	print("Project on github: https://github.com/javid-aliyev/Todo-list-application-Python")
	print("The documentation is in doc/ repo's dir")
	for index, command in enumerate(commands, 1):
		print(f"{index}. {command}")

def process_task_or_index(id2task, command, account, fn, done=None):
	# FIX: THIS FUNCTION IS NOT READABLE
	if command == "rm":
		task = _sinput("task to remove? ").strip()
		try:
			if task[0] == "\\":
				fn(task[1:], account)
			else:
				try:
					fn(id2task.get(int(task))[0], account)
				except (ValueError, TypeError):
					return
		except IndexError:
			pass
	else:
		task = _sinput("task? ").strip()
		try:
			if task[0] == "\\":
				fn(task[1:], account, done=done)
			else:
				try:
					fn(id2task.get(int(task))[0], account, done=done)
				except ValueError:
					pass
		except IndexError:
			pass

# ========
# Messages
# ========
# ========
@red_output
def warn(*args, **kwargs):
	"""Displays a warning
	:param args: list (stores str elements)
	:param kwargs: dict (stores extra keyword params of the print function)
	"""
	print(*args, **kwargs)

error = warn # error function

@blue_output
def info(*args, **kwargs):
	"""Displays an information
	:param args: list (stores str elements)
	:param kwargs: dict (stores extra keyword params of the print function)
	"""
	print(*args, **kwargs)

@green_output
def success(*args, **kwargs):
	"""Displays a success message
	:param args: list (stores str elements)
	:param kwargs: dict (stores extra keyword params of the print function)
	"""
	print(*args, **kwargs)
