"""Some utils for project"""

import platform
import os

OS = platform.system().lower()

def sinput(ps):
	"""Smart Input handles errors"""
	try:
		npt = input(ps).strip()
		return npt
	except (KeyboardInterrupt, EOFError):
		return

def clear_console():
	if OS == "windows":
		os.system("cls")
	else:
		os.system("clear")