"""Some utils for project"""

import platform
import os
import getpass
import json
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

# ========
# Messages
# ========
# ========
@red_output
def warn(warning):
	"""Displays warning
	:param warning: str
	"""
	print(warning)

error = warn # error function

@blue_output
def info(information):
	"""Displays information
	:param info: str
	"""
	print(information)

@green_output
def success(success):
	"""Displays success message
	:param success: str
	"""
	print(success)