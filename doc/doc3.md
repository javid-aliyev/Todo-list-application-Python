# Accounts
When you start the program, you are on the `guest` account. This account is shared by all users. You can create your own account or switch to an existing one if you know its password. Also you can't delete `guest` account

guest account's password: __root__

## Commands related to account management
| Command | Service                                     |
|---------|---------------------------------------------|
| addacc  | creates an account                          |
| rmacc   | removes an account                          |
| lsaccs  | shows all existing accounts                 |
| login   | to switch to an another account             |
| whoami  | shows which account is active at the moment |

## Extra information
_Info_: You can also use the account feature not only if several users on the same device run the program at different times, but even when one user has several tasks that are related, for example, with different projects, etc.
Also you can make several accounts for yourself (javid.open, javid.private)

# Tasks
Tasks are associated with an account

## Commands related to task management
| Command | Service                                                 |
|---------|---------------------------------------------------------|
| add     | adds a task to task list                                |
| rm      | removes a task from task list (by id or full task name) |
| rmall   | removes all tasks from task list                        |
| ls      | displays all tasks (and their status)                   |
| done    | marks the task as completed                             |
| undone  | marks the task as not completed                         |

## Extra information
Extra info:
1. If the ls command displayed the task green then the task is done. Otherwise it is not

## Task status
Task statuses: `done` or `in-progress`