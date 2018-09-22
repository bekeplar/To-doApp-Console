accounts = {}
todo_list = []


def create_task(task):
    """
    Adds the user's task to the to-do list"""

    todo_list.append(task)


 def delete_task(task):
    """
    Deletes a specific task from the todo list"""

    todo_list.remove(task)   


