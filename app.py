import sqlite3
import colorama as col
from sys import exit
from os import system

from utils.colorama_functions import *
from utils.tasks_crud import *

col.init() # intialyizing the colorama module

# shows all functionality of the application
def docs():
    make_green()
    print("\nDOCUMENTATION. Commands and instructions how to use them.")
    print("You use commands to edit your tasks list.")
    print("\n<command>  --  <information about command>\n")
    print("add    --  Shows you field where you can type new task you should to do.")
    print("del    --  Removes the task from the list. Just type task you want to remove in field.")
    print("delall --  Removes all tasks from the list.")
    print("edit   --  Type in the 1st field which task you want to edit. 2nd field - new task title.")
    print("all    --  Returns you all tasks you have.\n")
    print(".clear --  Clears the console.")
    print(".exit  --  You can quite the program using this command.")
    print(".help  --  Shows you documentation.\n")
    print("Also you can quite the program using shortcuts 'CTRL + C' or 'COMMAND + C'.")
    print("Or you can use '.exit' command.\n")
    resetall()

# main function
def main():
    print("'.help' command for more info.") # introduction

    # DATABASE CONNECTION
    connection = sqlite3.connect("database.db")
    c = connection.cursor()

    while True: # main loop
        try:
            inp = input("~ ").strip() # strip() function will remove leading and trailing whitespaces.
        except KeyboardInterrupt: # CTRL/COMMAND + C
            connection.close() # closing connection with database
            exit()

        # commands
        if inp == "add": add_task(c)
        elif inp == "all": read_all_tasks(c)
        elif inp == "del": del_task(c)
        elif inp == "delall": del_all_tasks(c)
        elif inp == "edit": edit_task(c)
        elif inp == ".help": docs()
        elif inp == ".clear": system("cls")
        elif inp == ".exit": exit()
        elif inp == "": continue
        else: print_red_resetall("No such command.")

        connection.commit() # saving (commiting) changes

if __name__ == "__main__":
    main()
