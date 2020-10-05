import os
from pathlib import Path

# ----------------
# database
# ----------------
DB_DIR_NAME = ".to-do-list-application"

DB_PARENT_DIR = str(Path.home())
DB_PATH = os.path.join(DB_PARENT_DIR, DB_DIR_NAME)

DB_JSON_PATH = os.path.join(DB_PATH, "json")
DB_LOGS_PATH = os.path.join(DB_PATH, "logs") # it does not exist yet

TASKS_JSON = os.path.join(DB_JSON_PATH, "tasks.json")
ACCOUNTS_JSON = os.path.join(DB_JSON_PATH, "accounts.json")

# (sha256) hashed password of db
DB_PASS = "7c7853e3659d1c01e65f3cb460ac07d079288bfa5bc21aae3d31fe01a0814278"

# ----------------
# core
# ----------------
COMMANDS = [
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