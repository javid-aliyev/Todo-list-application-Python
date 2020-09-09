"""
config file for database
"""
import os
from pathlib import Path

# Also we could set DB_PARENT_DIR as (5):
# f"/home/{os.login()}/"
# os.path.expanduser("~")
# os.environ["HOME"]
# str(Path.home())
# f"/home/{os.environ['USER']}"

DB_DIR_NAME = ".to-do-list-application"

DB_PARENT_DIR = str(Path.home())
DB_PATH = os.path.join(DB_PARENT_DIR, DB_DIR_NAME) # f"/home/{os.login()}/.to-do-list-application/"

DB_JSON_PATH = os.path.join(DB_PATH, "json")
DB_LOGS_PATH = os.path.join(DB_PATH, "logs") # it does not exist yet

DB_JSON_TASKS_PATH = os.path.join(DB_JSON_PATH, "tasks.json")
DB_JSON_ACCOUNTS_PATH = os.path.join(DB_JSON_PATH, "accounts.json")
DB_JSON_CORE_PATH = os.path.join(DB_JSON_PATH, "core.json")