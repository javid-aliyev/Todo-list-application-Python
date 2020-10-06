# Project File/Folder Structure
| Folder/File      | Service                                       |
|------------------|-----------------------------------------------|
| doc/             | documentation                                 |
| app.py           | program's entry point (run it)                |
| account.py       | Account class                                 |
| task.py          | Task class                                    |
| decorators.py    | colored output decorators (colorama required) |
| tools.py         | some tools                                    |
| db_creator.py    | creates a database                            |
| config.py        | project configuration file                    |
| requirements.txt | requirements file                             |

# Where is the database located?
It is located in the home dir: `$HOME/.to-do-list-application`

# Data in db?
| File              | Service                                                 |
|-------------------|---------------------------------------------------------|
| json/account.json | accounts and their hashed passwords                     |
| json/tasks.json   | accounts' tasks and their statutes                      |

## Extra info
1. Passwords in account.json are hashed