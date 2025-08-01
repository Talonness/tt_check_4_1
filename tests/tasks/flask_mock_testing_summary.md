# What We Did: Mock Services and Route Testing in Flask

## Implemented a Mock Service
We created a `MockTaskService` that mimics the real `TaskService` but only stores tasks in memory (RAM), not in files or a database.

## Injected the Mock into the App
We updated our Flask app factory (`create_app`) to accept any service, so we can swap in the mock for testing.

## Wrote Route Tests Using the Mock
We wrote tests that use Flask’s test client to interact with the API routes, verifying that adding, completing, and deleting tasks works as expected—without touching real data files.

---

# Why This Helps SQA and Software Testing

- **Isolation:** Tests run in a clean, controlled environment. No real files or databases are changed, so tests are safe and repeatable.
- **Speed:** In-memory mocks are much faster than file or database operations, so tests run quickly.
- **Reliability:** Each test starts with a blank slate, so results are consistent and not affected by leftover data from previous tests.
- **Realism:** By using the test client to make HTTP requests, we test the app the same way a real user or frontend would interact with it.

---

# Example: Real Service vs. Mock Service

| Scenario           | Real Service (File/DB) | Mock Service (In-Memory) |
|--------------------|------------------------|--------------------------|
| Add a task         | Writes to tasks.json   | Adds to a Python list    |
| Complete a task    | Updates file/database  | Updates a Python dict    |
| Test speed         | Slower (disk I/O)      | Fast (RAM only)          |
| Test isolation     | Needs cleanup/reset    | Always clean per test    |
| Risk of data loss  | Possible if test fails | No risk, nothing permanent |

---

# Example Test (with Mock)

```python
def test_add_task_route_uses_service(app_with_mock):
    client = app_with_mock.test_client()
    response = client.post('/api/tasks', json={"title": "Mock Task"})
    assert response.status_code == 201
    # Fetch tasks using the API, just like a real user would
    tasks_response = client.get('/api/tasks')
    tasks = tasks_response.get_json()
    assert any(task["title"] == "Mock Task" for task in tasks)
```

---

# Key Takeaways for Beginners

- **Always use the test client** to interact with your Flask app in tests. This simulates real user/API behavior.
- **Mocks make tests safe and fast.** You can test all logic without worrying about breaking real data.
- **Dependency injection** (passing in the service) lets you swap between real and mock services easily, making your app more testable and flexible.
