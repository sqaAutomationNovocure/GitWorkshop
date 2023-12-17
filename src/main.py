# main.py

def add_task(task_list, task):
    """Adds a new task to the task list."""
    if task:
        task_list.append(task)
    return task_list


def delete_task(task_list, task):
    """Deletes a specified task from the task list."""
    if task in task_list:
        task_list.remove(task)
    return task_list


def view_tasks(task_list):
    """Returns a string representation of all tasks in the task list."""
    return '\n'.join(f"{index + 1}: {task}" for index, task in enumerate(task_list))


