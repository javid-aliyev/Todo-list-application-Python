from .colorama_functions import *

# CRUD; argument c -> cursor
def add_task(c):
    try:
        task = input("Enter new task's name: ").strip()
    except KeyboardInterrupt:
        return

    # sql query for checking if there is another task with such title
    test_sql = "SELECT title FROM tasks WHERE title = '" + task + "'"
    if c.execute(test_sql).fetchone():
        print_red_resetall("There is a task with such title.")
        return

    if task != "":
        sql = "INSERT INTO tasks ('title') VALUES ('" + task + "')" # main sql query
        print("Task '" + task + "' was created!")
        c.execute(sql)
    else: print("I can not add empty task.")

def del_task(c):
    read_all_tasks(c)

    try:
        task = input("Which task you want to delete? ").strip()
    except KeyboardInterrupt:
        return

    tasks = get_all_tasks(c)
    if not task in tasks:
        print_red_resetall("No such task.")
        return
    else:
        sql = "DELETE FROM tasks WHERE title = '" + task  + "'"
        c.execute(sql)
        print("The task '" + task + "' was deleted.")

def del_all_tasks(c):
    read_all_tasks(c)

    try:
        q = input("Do you actually want to remove all tasks? (Y/n) ")
    except KeyboardInterrupt:
        return

    if q.lower() == "y":
        sql = "DELETE FROM tasks"
        c.execute(sql)

def edit_task(c):
    read_all_tasks(c)

    try: task = input("Which task you want to edit? ").strip()
    except KeyboardInterrupt: return

    tasks = get_all_tasks(c)

    if not task in tasks:
        print_red_resetall("No such task.")
        return

    try: new_title = input("New title for '" + task + "' task? ").strip()
    except: return

    if not new_title in tasks:
        sql = "UPDATE tasks SET title = '" + new_title + "' WHERE title = '" + task + "'"
        c.execute(sql)
        print("Task '" + task + "' was edited to '" + new_title + "'.")

def read_all_tasks(c):
    """ Prints all tasks """
    print("\nAll tasks:")
    tasks = get_all_tasks(c)
    for task in tasks:
        print_blue("* " + task)
    resetall()

# returns a list of tasks
def get_all_tasks(c):
    """ Returns all tasks from database as list with tasks title """
    arr = []
    query = c.execute("SELECT * FROM tasks")
    for i in query:
        arr.append(i[1])
    return arr