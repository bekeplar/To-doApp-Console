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


def mark_as_finished(task):
    """Makks a task from the to-do list as finished"""

    task_name = task_list.name(task)
    todo_list[task_name] = task + " [finished]"


def delete_all_tasks():
    """Deleting the entire list on the user's account."""

    todo_list.clear()    
