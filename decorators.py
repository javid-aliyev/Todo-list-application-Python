"""Colored output decorators"""

import colorama
import functools

colorama.init()

def green_output(fn):
	@functools.wraps(fn)
	def wrapper(*args, **kwargs):
		print(colorama.Fore.GREEN, end="")
		result = fn(*args, **kwargs)
		print(colorama.Style.RESET_ALL, end="")
		return result
	return wrapper

def red_output(fn):
	@functools.wraps(fn)
	def wrapper(*args, **kwargs):
		print(colorama.Fore.RED, end="")
		result = fn(*args, **kwargs)
		print(colorama.Style.RESET_ALL, end="")
		return result
	return wrapper
