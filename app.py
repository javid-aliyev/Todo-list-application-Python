"""Main module"""

import sys

import utils
from tasks import Tasks

class Program:
    def __init__(self):
        self.main()

    def execute_command(self, command):
        """Executes the command"""
        if command == "add":
            task = utils.sinput("task: ")
            Tasks.add(task)
        elif command == "tasks":
            Tasks.print()
        elif command == "delete":
            task = utils.sinput("task: ")
            Tasks.delete(task)
        elif command == "deltasks":
            Tasks.delete_tasks()
        elif command == ":quit":
            sys.exit()
        elif command == ":clear":
            utils.clear_console()
        elif command == "":
            return
        else:
            print("no such command")

    def main(self):
        while True:
            command = utils.sinput("# ")
            self.execute_command(command)

if __name__ == "__main__":
    Program()