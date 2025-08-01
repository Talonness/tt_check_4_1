# ✅ Task Tracker Test Cases – Master Reference

This document contains all implemented and planned test cases grouped by functional area, based on user stories and refactor goals.

---

## ✅ User Story Test Cases

### 📌 US002 – Add Task

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US002-001     | Add valid task                       | Automated        | Basic happy path                       |
| TC-US002-002     | Missing title                        | Automated        | Should return 400                      |
| TC-US002-003     | Empty title                          | Automated        | Should return 400                      |
| TC-US002-004     | Missing description                  | Automated        | Optional field                         |

---

### 📌 US003 – View Tasks

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US003-001     | View tasks when none exist           | Automated        | Should return empty list (`[]`)       |
| TC-US003-002     | View tasks when tasks exist          | Automated        | Should return list of task objects     |

---

### 📌 US004 – Mark Task Complete

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US004-001     | Mark task complete (valid ID)        | Automated        | Expects 200 and `"completed": true`    |
| TC-US004-002     | Mark task complete (nonexistent ID)  | Automated        | Expects 404 Not Found                  |

---

### 📌 US005 – Delete Task

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US005-001     | Delete task (valid ID)               | Automated        | Should return 200                      |
| TC-US005-002     | Delete task (nonexistent ID)         | Automated        | Should return 404                      |

---

### 📌 US011 – Persist Tasks (File Storage)

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US011-001     | Tasks persist after restart          | Automated        | Check `tasks.json` after POST          |
| TC-US011-002     | Load tasks from file on startup      | Automated        | File used as source of truth           |

---

### 📌 US006 – UI for Add Task (CLI Stub)

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US006-001     | CLI prompt accepts task input        | Manual           | Uses `input()` in CLI stub             |
| TC-US006-002     | CLI task passed to service           | Manual           | Requires verifying console output      |

---

### 📌 US027 – View Task Report (via CLI)

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US027-001     | CLI lists tasks                      | Manual           | Read-only task display                 |

---

### 📌 US028 – CLI Complete Task

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US028-001     | CLI marks task as complete           | Manual           | Verifies behavior of `TaskService`     |

---

## ✅ Error Handling & Validation (US014, US015)

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US015-001     | Invalid JSON format                  | Automated        | Expects 400 Bad Request                |
| TC-US015-002     | Missing JSON content-type header     | Automated        | Expects 415 Unsupported Media Type     |
| TC-US015-003     | PUT/DELETE with invalid ID           | Automated        | Expects 404 Not Found                  |

---

## ✅ Architecture & Refactor Test Cases

### 🧱 Blueprint Routing (RF001)

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-ARCH-001      | Routes use Blueprints                | Manual/Static    | `main.py` registers blueprints only    |
| TC-ARCH-002      | No route defined in `main.py`        | Manual/Static    | All routes moved to `routes/`          |
| TC-NFR001-001 | Confirm all routes are available via Blueprint | Automated | GET, POST, PUT, DELETE all succeed via `/api/tasks` endpoints |

---

### 🧱 File Storage Refactor (RF002)

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-ARCH-003      | `task_storage.py` reads from file    | Automated        | Check that it returns task list        |
| TC-ARCH-004      | `task_storage.py` writes to file     | Automated        | Should save tasks after add/delete     |

---

### 🧱 App Factory Pattern

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-ARCH-005      | App initializes via `create_app()`   | Automated        | Used in tests via `conftest.py`        |
| TC-ARCH-006      | Blueprint registration verified      | Automated        | Tests confirm endpoints are mounted    |
| TC-NFR001-002 | Test `create_app()` correctly registers Blueprints | Automated | No 404 errors from misrouting; routes mounted without exception |

---

### 🧱 TaskService OOP Refactor (Sprint 3+)

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-RF004-001     | TaskManager adds task                | Automated        | Unit test `add_task()` logic           |
| TC-RF004-002     | TaskManager marks task complete      | Automated        | Unit test `complete_task()` logic      |
| TC-RF004-003     | TaskManager deletes task             | Automated        | Unit test `delete_task()` logic        |
| TC-RF004-004 | Validate `Task` class instantiation and attributes | Automated | Checks ID, title, description, and completed status |

---

### 🧱 TaskService Class Refactor (RF005) — **New Subsection**

| Test Case ID | Description                                 | Test Type | Notes                                       |
| ------------ | ------------------------------------------- | --------- | ------------------------------------------- |
| TC-RF005-001 | `TaskService.add_task()` stores task        | Automated | Returns correct task with ID and title      |
| TC-RF005-002 | `TaskService.get_tasks()` returns task list | Automated | Should return all tasks from in-memory list |
| TC-RF005-003 | `TaskService.update_task()` updates task    | Automated | Updates completion status to `True`         |
| TC-RF005-004 | `TaskService.delete_task()` removes task    | Automated | Task is removed and no longer in list       |

---

## ✅ Integration & API Layer Tests (Sprint 3+)

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-RF008-001     | Add task via `requests.post()`       | Automated (requests) | Integration test for POST             |
| TC-RF008-002     | View task via `requests.get()`       | Automated (requests) | Integration test for GET              |
| TC-RF008-003     | Complete task via `requests.put()`   | Automated (requests) | Integration test for PUT              |
| TC-RF008-004     | Delete task via `requests.delete()`  | Automated (requests) | Integration test for DELETE           |

---

## ✅ Manual Tests via Postman or CLI

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-MANUAL-001    | Add task via Postman/curl            | Manual           | Screenshot required                    |
| TC-MANUAL-002    | View tasks via Postman/curl          | Manual           | Screenshot required                    |
| TC-MANUAL-003    | Mark task complete via Postman       | Manual           | Verifies PUT endpoint                  |
| TC-MANUAL-004    | Delete task via Postman              | Manual           | Verifies DELETE endpoint               |

---


