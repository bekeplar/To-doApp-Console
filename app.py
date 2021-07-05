from tasks import *
from accounts import *


def start_func():
    name = input("Please enter your name here: ")
    password = input("Please enter your password ")
    print("you have successfully logged in")
    main_func(name, password)

def main_func(name, password):
    while True:
        if password not in accounts:
            add_account(name, password)
            print("you are currently logged in!")
            print("Please select what you want to do!")
            print(" 1. Add a task")
            print("2. Mark a task as finished.")
            print("3. Delete a task")
            print("4. Delete all tasks")
            #prompting the user for input
            selection = input("Your selection: ")
            if selection == "1":
                task = input("Please enter your task here:")
            # Marking a task finished    
            elif selection == "2":
                print(todo_list)
                task = input("Please enter the task you want to delete here: ")
    
                print("your task has been successfully completed")
                #Deleting a specific task
            elif selection == "3":
                
                print("Your task has been successfully deleted")
            elif selection == "4":
                print(todo_list)
                task = input("Please confirm your decission: ")
                
                print("Your tasks have been successfully deleted")
            else:
                print("Please enter a selection from the listed options")
        

if __name__ == "__main__":
    start_func()