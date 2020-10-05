"""Some tools for the project"""

import platform
import os
import getpass
import sys
import json

from decorators import *
import config

# ================================
# Input
# ================================
# ================================
# ================================
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

# ================================
# Clear console
# ================================
# ================================
# ================================
if platform.system().lower() == "windows":
	def _clear_console():
		"""Clears the console"""
		os.system("cls")
else:
	def _clear_console():
		"""Clears the console"""
		os.system("clear")

# ================================
# Help function
# ================================
# ================================
# ================================
def _print_help_info():
	"""Prints help pages"""
	print("Project on github: https://github.com/javid-aliyev/Todo-list-application-Python")
	print("The documentation is in doc/ repo's dir")
	for index, command in enumerate(config.COMMANDS, 1):
		print(f"{index}. {command}")

# ================================
# JSON
# ================================
# ================================
# ================================
def get_json_from_file(path):
	"""Fetches data from a json file
	param path is path to file
	:param path: str
	:return: str
	"""
	with open(path, "rt") as jfl:
		return json.load(jfl)

def save_json_to_file(path, data):
	"""Saves new data to a json file
	param path is path to file
	param data is json
	:param path: str
	:param data: str
	"""
	with open(path, "wt") as jfl:
		json.dump(data, jfl, indent=4)

# ================================
# Messages
# ================================
# ================================
# ================================
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

# ================================
# Other
# ================================
# ================================
# ================================
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