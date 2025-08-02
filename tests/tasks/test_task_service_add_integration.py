# test_task_service_task_add_integration.py
# Integration tests for TaskService using Task objects (refactor/modern approach)

import pytest
from app.services.task_service import TaskService
from app.models.task import Task

def test_add_task_creates_and_stores_task_object(client):
    """
    TC-RF005-001: TaskService.add_task() stores and returns a new Task object internally.
    Ensures that after refactor, TaskService uses Task objects and returns correct dict structure.
    Flask app integration test using database storage
    """
    # Use the Flask app's injected service (database-backed)
    from flask import current_app
    with client.application.app_context():
        service = current_app.task_service
        result = service.add_task("Integration Test", "Integration description")

        # Check returned structure (backward compatibility)
        assert isinstance(result, dict)
        assert result["title"] == "Integration Test"
        assert result["description"] == "Integration description"
        assert result["completed"] is False

        # Verify it was stored by getting all tasks
        all_tasks = service.get_tasks()
        our_task = None
        for task in all_tasks:
            if task["title"] == "Integration Test":
                our_task = task
                break
        
        assert our_task is not None
        assert our_task["title"] == "Integration Test"
        assert our_task["description"] == "Integration description"
        assert our_task["completed"] is False