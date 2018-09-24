import time
from tasks import *
from accounts import *


if __name__ == "__main__":
    while True:
            name = input("Please enter your name here: ")
            password = input("Please enter your password ")

            if password not in accounts:
                add_account(name, password)
                print("A new account was created for you!")
                print("Please select what you want to do!")
                print(" 1. Add a task")
                print("2. Mark a task as finished.")
                print("3. Delete a task")
                print("4. Delete all tasks")

                selection = input("Your selection: ")
                if selection == "1":
                    task = input("Please enter your task here:")
                    create_task(task)
                elif selection == "2":
                    print(todo_list)
                    task = input("Please enter the task you want to delete here: ")
                    delete_task(task)
                elif selection == "3":
                    delete_all_tasks()
                elif selection == "4":
                    print(todo_list)
                    task = input("Please enter the task you want to mark finished: ")
                    mark_as_finished(task)
                else:
                    print("Please enter a selection from the listed options")
            else:
                login_func()