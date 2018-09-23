import time
from accounts import *
from tasks import *

select = {
    1: "Create task",
    2: "Delete task",
    3: "Delete all tasks",
    4: "Mark task as finished",
    5: "Display all tasks",
    6: "Logout"
}


def main():
    print("\nselect")
    for key, value in select.items():
        print("{}. {}".format(key, value))

    selected_option = input("\nSelect an option: ")
    try:
        selected_option = int(selected_option)

        """  Check if the selected option exists on the task list"""
        select_options = list(select.keys())
        if selected_option not in select_options:
            print(":The selected item does not exists\n")
            

        if selected_option == 1:
            task = input("\nEnter your task: ")
            print("updating tasks...")
            time.sleep(2)

            """ Create a new task """
            result = create_task(task)
            print(":{}\n".format(result[0]))
            

        if selected_option == 2:
            """  Check if the todo list is empty"""
            if is_list_empty():
                print(":Your todo list is empty")
                

            """ Print a list of todos"""
            display_todo_list()

            selected_task = input("\nSelect a task to delete: ")
            print(": Deleting task...")
            time.sleep(2)

            """ Check if the seleted item is on the list"""
            task_position = int(selected_task) - 1
            if not is_task_in_the_list(task_position):
                print(":The selected task is not on the list\n")
                

            """ Delete the selected task from the list"""
            result = delete_task(todo_list[task_position])
            print(": {}\n".format(result[0]))
            

        if selected_option == 3:
            """ Check if the todo list is empty"""
            if is_list_empty():
                print(": There are no items in your todo list")
                

            print("\nDeleting all tasks...")
            time.sleep(2)

            """ Delete all tasks from the todo list"""
            delete_all_tasks()
            print("Tasks have been deleted successfully\n")
        

        if selected_option == 4:
            """ Check if the todo list is empty"""
            if is_list_empty():
                print(" Your todo list is empty")
                

            """ Displaying a list of todos"""
            display_todo_list()

            selected_task = input("\nSelect a finished task: ")
            print(": Marking task as finished...")
            time.sleep(2)

            """ Check if the seleted task is on the list"""
            task_position = int(selected_task) - 1
            if not is_task_in_the_list(task_position):
                print(": The selected task does not exist on list\n")
                

            """ Mark task as finished"""
            result = mark_as_finished(todo_list[task_position])
            print(": {}\n".format(result[0]))
            main()

        if selected_option == 5:
            """ Check if the todo list is empty"""
            if is_list_empty():
                print("There are no items in your todo list")
                

            """ Display all items in the todo list"""
            display_todo_list()
            

        if selected_option == 6:
            print("\n:Logging out...")
            time.sleep(2)
            print(": You have been logged out\n")
            return

    except ValueError:
        print(": Your option should be a number\n")
        


if __name__ == "__main__":
    """user inputs credentials"""

    print("\n<-> Welcome to my todo App <->\n")
    name = input("Enter your name: ")
    password = input("Enter password: ")

    if login(name, password):
        print(": Logging in...")
        
    else:
        """"  Signingup for an account for the user"""
        print(": Registering user...")
        time.sleep(2)
        add_account(name, password)
        print(": User registered successfully\n")
        