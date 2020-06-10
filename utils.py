"""Some utils for project"""

import platform
import os
import getpass

OS = platform.system().lower()

def sinput(ps):
	"""Smart Input handles errors"""
	try:
		npt = input(ps).strip()
		return npt
	except (KeyboardInterrupt, EOFError):
		return

def secured_sinput(ps):
	try:
		npt = getpass.getpass(ps).strip()
		return npt
	except (KeyboardInterrupt, EOFError):
		return

def clear_console():
	if OS == "windows":
		os.system("cls")
	else:
		os.system("clear")

def print_help_info(commands):
	print("Documentation: https://github.com/javid-aliyev/Todo-list-application-Python")
	for index, command in enumerate(commands, 1):
		print(f"{index}. {command}")