# test_task_service_get_integration.py
# Integration tests for TaskService.get_tasks() with Task class (RF004)

import pytest
from app.services.task_service import TaskService
from app.models.task import Task

def test_get_tasks_when_none_exist_integration(client):
    """
    TC-RF004-002 (integration)
    Integration test for TaskService.get_tasks() when no tasks exist (Task object refactor)
    Flask app integration test using database storage
    """
    # Use the Flask app's injected service (database-backed)
    from flask import current_app
    with client.application.app_context():
        service = current_app.task_service
        tasks = service.get_tasks()
        assert isinstance(tasks, list)
        assert tasks == []

def test_get_tasks_returns_added_tasks_integration(client):
    """
    TC-RF004-002 (integration)
    Integration test for TaskService.get_tasks() after adding tasks (Task object refactor)
    Flask app integration test using database storage
    """
    # Use the Flask app's injected service (database-backed)
    from flask import current_app
    with client.application.app_context():
        service = current_app.task_service
        task1 = service.add_task("Task1", "Grocery")
        task2 = service.add_task("Task2", "Study")
        all_tasks = service.get_tasks()

        # Should return list of dicts (backward compatibility)
        assert isinstance(all_tasks, list)
        assert len(all_tasks) >= 2

        # Check dict structure - INSIDE the app_context
        for task in all_tasks:
            assert set(task.keys()) == {"id", "title", "description", "completed"}

        # Check values
        titles = [task["title"] for task in all_tasks]
        assert "Task1" in titles
        assert "Task2" in titles
        
        # Verify task structure and data integrity
        for task in all_tasks:
            assert "id" in task
            assert "title" in task
            assert "description" in task
            assert "completed" in task
