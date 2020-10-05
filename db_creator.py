"""
Creates json files in json/ dir
"""

import os
import json
import hashlib

from tools import info, success, warn, error, _sinput, _secured_sinput
from config import *


def create_database():
	# DB_PATH directory and DB_PATH/json
	try:
		os.chdir(DB_PARENT_DIR) # cd $HOME
		os.mkdir(DB_DIR_NAME) # mkdir .to-do-list-application/
		os.chdir(DB_PATH) # cd $HOME/.to-do-list-application
		os.mkdir("json")
	except FileExistsError:
		pass


	# json/accounts.json file
	accounts_json = os.path.join(DB_PATH, "json", "accounts.json")
	hashed_guest_password = hashlib.sha256("root".encode("utf8")).hexdigest()
	with open(accounts_json, "wt") as jfl:
		jfl.write(json.dumps({"guest": hashed_guest_password}, indent=4))


	# json/tasks.json file
	tasks_json = os.path.join(DB_PATH, "json", "tasks.json")
	with open(tasks_json, "wt") as jfl:
		jfl.write(
			json.dumps({
				"guest": {
					"test task #1": False,
					"test task #2": False
				}
			}, indent=4)
		)


if __name__ == "__main__":
	db_pass = _secured_sinput("password? ")
	if hashlib.sha256(db_pass.encode("utf8")).hexdigest() == DB_PASS:
		success("correct password")
		print("------------------")
		print(f"Do you actually want to create or overwrite the database({DB_PATH})? [y/n]")
		warn("!!that process will overwrite the database!!")
		npt = input()
		if len(npt) > 0 and npt[0].lower() != "n":
			create_database()
			success("(+) The database was created or overwritten")
		else:
			info("(=) Abort")
	else:
		error("wrong password!")

# if __name__ == "__main__":
# 	db_pass = secured_sinput("db password? ")
# 	if hashlib.sha256(db_pass.encode("utf8")).hexdigest() == config.DB_PASS:
# 		warn("!!that process will overwrite the database!!")
# 		print(f"Do you actually want to create or overwrite the database({config.DB_PATH})? [y/n]")
# 		npt = sinput("")
# 		if len(npt) > 0 and npt[0].lower() != "n":
# 			create_db()
# 			success("(+) The database was created or overwritten")
# 		else:
# 			info("(=) Abort")
# 	else:
# 		error("wrong password!")