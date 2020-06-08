"""
If there is no database.db in this project directory then you should run this
code. It will create the database and its tables (structure)
"""

import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE `tasks` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`task`	TEXT NOT NULL UNIQUE,
	`is_done`	INTEGER NOT NULL
);
""")
connection.commit()
connection.close()