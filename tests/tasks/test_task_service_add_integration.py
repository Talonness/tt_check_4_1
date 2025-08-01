# test_task_service_task_add_integration.py
# Integration tests for TaskService using Task objects (refactor/modern approach)

import pytest
from app.services.task_service import TaskService
from app.models.task import Task

def test_add_task_creates_and_stores_task_object():
    """
    TC-RF005-001: TaskService.add_task() stores and returns a new Task object internally.
    Ensures that after refactor, TaskService uses Task objects and returns correct dict structure.
    """
    service = TaskService(storage=None)
    result = service.add_task("Integration Test", "Integration description")

    # Check returned structure (backward compatibility)
    assert isinstance(result, dict)
    assert result["title"] == "Integration Test"
    assert result["description"] == "Integration description"
    assert result["completed"] is False

    # Check internal storage (Task object)
    assert hasattr(service, "_tasks")
    assert len(service._tasks) == 1
    assert isinstance(service._tasks[0], Task)
    assert service._tasks[0].title == "Integration Test"
    assert service._tasks[0].description == "Integration description"
    assert service._tasks[0].completed is False