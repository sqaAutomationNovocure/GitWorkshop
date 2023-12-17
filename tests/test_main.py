import pytest
from src.main import add_task, delete_task, view_tasks, clear_completed_tasks, get_task_count, complete_task


# Test data setup
@pytest.fixture
def task_list():
    return ["Task 1", "Task 2", "Task 3"]


# Test: Add a task
def test_add_task(task_list):
    new_task = "Task 4"
    updated_list = add_task(task_list, new_task)
    assert new_task in updated_list, "The new task should be added to the list"


# Test: Delete a task
def test_delete_task(task_list):
    task_to_delete = "Task 2"
    updated_list = delete_task(task_list, task_to_delete)
    assert task_to_delete not in updated_list, "The task should be deleted from the list"


# Test: View tasks
def test_view_tasks(task_list):
    expected_output = "1: Task 1\n2: Task 2\n3: Task 3\n"
    assert view_tasks(task_list) == expected_output, "The view should list all tasks correctly"


# Test: Add a task with empty name
def test_add_empty_task(task_list):
    new_task = ""
    updated_list = add_task(task_list, new_task)
    assert new_task not in updated_list, "Empty tasks should not be added"


# Test: Delete a non-existent task
def test_delete_nonexistent_task(task_list):
    nonexistent_task = "Task 999"
    updated_list = delete_task(task_list, nonexistent_task)
    assert len(updated_list) == len(task_list), "The task list should remain unchanged"


