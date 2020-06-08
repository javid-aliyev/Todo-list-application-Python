"""Access to the database - cursor"""

import sqlite3

class Database():
	def __init__(self, file="database.db"):
		self.file = file

	def __enter__(self):
		self.conn = sqlite3.connect(self.file)
		return self.conn.cursor()

	def __exit__(self, type, value, traceback):
		self.conn.commit()
		self.conn.close()
