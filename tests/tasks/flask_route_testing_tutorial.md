# Tutorial: Testing Flask Routes with Dependency Injection and Mocks

## Overview

This tutorial demonstrates how to write isolated, robust tests for Flask API routes using dependency injection and a mock service. The goal is to help SQA students and beginner testers understand best practices for route testing, context management, and the use of the Flask test client.

---

## Key Concepts

- **Dependency Injection (DI):** Injecting a mock service into the Flask app for testing, instead of using the real service.
- **Mock Service:** An in-memory, fake version of your service that allows for isolated, repeatable tests.
- **Flask Test Client:** A special client provided by Flask to simulate HTTP requests to your app, just like a real user or API consumer.
- **Context Isolation:** Ensuring each test runs in its own context, preventing state leakage between tests.

---

## Example: `test_routes_with_mock.py`

Below is a simplified and annotated version of the test file.

```python
import pytest
from app import create_app
from tests.conftest import MockTaskService

# Fixture: Creates a Flask app with the mock service injected
@pytest.fixture()
def app_with_mock():
    app = create_app(service=MockTaskService())
    app.config['TESTING'] = True
    return app

# Test: Adding a task via the API
def test_add_task_route_uses_service(app_with_mock):
    client = app_with_mock.test_client()
    response = client.post('/api/tasks', json={"title": "Mock Task", "description": "Test DI"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Mock Task"
    assert data["description"] == "Test DI"
    assert data["completed"] is False

    # IMPORTANT FOR BEGINNERS:
    # Always use the test client to fetch data, not direct service access!
    tasks_response = client.get('/api/tasks')
    tasks = tasks_response.get_json()
    assert any(task["title"] == "Mock Task" for task in tasks)

    # Test error handling for missing title
    response2 = client.post('/api/tasks', json={"description": "No title here"})
    assert response2.status_code == 400
    error = response2.get_json()
    assert "error" in error and error["error"] == "Title is required"

# Test: Completing a task via the API
def test_complete_task_route_with_mock(app_with_mock):
    client = app_with_mock.test_client()
    response = client.post('/api/tasks', json={"title": "Finish Lab", "description": "Complete Sprint 3 Lab 2"})
    assert response.status_code == 201
    t = response.get_json()
    task_id = t["id"]

    resp = client.put(f'/api/tasks/{task_id}')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["id"] == task_id
    assert data["completed"] is True

    # Test completing a non-existent task
    resp2 = client.put('/api/tasks/999')
    assert resp2.status_code == 404
    err = resp2.get_json()
    assert err["error"] == "Task not found"

# Test: Deleting a task via the API
def test_delete_task_route_with_mock(app_with_mock):
    client = app_with_mock.test_client()
    resp1 = client.post('/api/tasks', json={"title": "Task A"})
    assert resp1.status_code == 201
    resp2 = client.post('/api/tasks', json={"title": "Task B"})
    assert resp2.status_code == 201
    t2 = resp2.get_json()
    task_id = t2["id"]

    resp = client.delete(f'/api/tasks/{task_id}')
    assert resp.status_code == 200
    msg = resp.get_json()
    assert msg == {"message": "Task deleted"}

    # Verify task is removed using the test client
    tasks = client.get('/api/tasks')
    titles = [t["title"] for t in tasks.get_json()]
    assert "Task B" not in titles

    # Test deleting a non-existent task
    resp2 = client.delete(f'/api/tasks/{task_id}')
    assert resp2.status_code == 404
    err = resp2.get_json()
    assert err["error"] == "Task not found"
```

---

## Best Practices Highlighted

- **Always use the test client for all API interactions.**  
  This ensures your tests reflect real user/API behavior and avoids Flask context issues.
- **Never access the service or app state directly in route tests.**  
  This can lead to confusing bugs due to Flask's request/app context isolation.
- **Use fixtures to inject mocks and configure your app for testing.**
- **Test both success and error cases for each route.**

---

## Why Use Mocks and the Test Client?

- **Mocks** allow you to test your routes in isolation, without touching real data or files.
- **The test client** simulates real HTTP requests, ensuring your tests are as close as possible to real-world usage.
- **Context isolation** prevents state leakage and makes your tests reliable and repeatable.

---

## Summary for SQA/Testers

- Use dependency injection to swap real services for mocks in tests.
- Always interact with your Flask app through the test client in route tests.
- Test both normal and error scenarios.
- Add comments to help future testers understand the reasoning behind your approach.

---

This approach will help you write robust, maintainable, and educational tests for your Flask APIs!
