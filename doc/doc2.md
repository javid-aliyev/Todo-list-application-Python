# Project File/Folder Structure
| Folder/File    | Service                                         |
|----------------|-------------------------------------------------|
| doc/           | documentation                                   |
| app.py         | program's entry point (run it, also needs sudo) |
| account.py     | Account class                                   |
| task.py        | Task class                                      |
| decorators.py  | colored output decorators (colorama required)   |
| tools.py       | some tools                                      |
| db_creator.py  | creates a database                              |
| db_config.py   | database configuration file                     |

# Where is the database located?
On UNIX-like systems, the database is located in the `/opt/to-do-list-application/` (if you ran `sudo python3 db_creator.py`) directory.
JSON files and possible logs are stored here.