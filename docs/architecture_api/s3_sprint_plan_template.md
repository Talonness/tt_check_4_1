# Sprint 3 OOP Refactor, TaskService Class, and `requests` API Tests

## 🎯 Sprint Goal
This sprint introduces foundational architecture improvements to support future features. You will separate business logic from Flask routes using a `TaskService` class and a persistence interface (`TaskRepository`). You will also implement CLI-based task completion and introduce automated API testing using the `requests` library.

## 🧭 Educational Context

Why this sprint matters:

* Introduces **Object-Oriented Programming (OOP)** to centralize task logic in a `TaskService` class.
* Emphasizes testability and reusability through class-based design.
* Begins decoupling storage from logic to support swapping the JSON file for a database in Sprint 4.
* Teaches how to write **automated API tests** using `requests`, moving away from manual tools like Postman and curl.
* Keeps CLI available for transitional manual testing—but it will be deprecated in Sprint 4.
* Reinforces single responsibility and modular design to support growing complexity.

> This is a foundational architecture sprint that enables database integration, web UI development, and automated system testing in future sprints.


## Sprint Goals Overview

## Sprint Goals Overview

Sprint 3 focuses on preparing the application for future growth by transitioning from procedural design to object-oriented architecture. The goals for this sprint are reflected in the Refactor IDs (RF00X) below and include:

* Introduce `TaskService` to encapsulate task logic
* Implement `TaskRepository` interface to decouple persistence
* Modularize route logic with Flask Blueprints
* Use dependency injection via `create_app()` for wiring services
* Replace CLI test cases with automated API tests using `requests` (US035)

## User Stories

- ✅ **US011 – Persist Tasks**: Already implemented (Sprint 2, supports refactor)
- ✅ **US027 – View Task Report (CLI)**: Supports CLI-to-UI migration in Sprint 4
- ✅ **US028 – CLI Logic (Add/View/Quit)**: Fully implemented
- 🆕 **US029 – CLI UI: Mark Task Complete**
  - Implemented in CLI and will later be deprecated when UI is available
- 🆕 **US035 – API Testing Automation (requests)**
  - Replace Postman/manual API tests with Python `requests`-based automation

## Refactors

| Refactor ID | Description                                     | Notes                                              |
|-------------|-------------------------------------------------|----------------------------------------------------|
| RF004       | Introduce `Task` class                          | Replace dictionary-based task model                |
| RF005       | Create `TaskService` class                      | Encapsulates all logic for add/view/edit/delete    |
| RF006       | Inject `TaskService` into route handlers        | Enables future testing and modularization          |
| RF007       | Blueprint Modularization                        | Separate task and health routes into Blueprints    |
| RF008       | Replace CLI Manual Tests with `requests` tests  | Transition to automated API testing (test_requests_api.py) |                   |

## Testing & Automation

-  Unit tests for `Task`, `TaskService`, and route handlers using `pytest`
-  Create `tests/api/test_requests_api.py` for API validation
-  Continue using `conftest.py` for test setup and cleanup
-  CLI testing will not be expanded — web UI and BDD to replace in Sprint 4+

## 5. CI/CD Updates

- Add `requests`-based API tests to GitHub Actions CI pipeline
- Track code coverage for service and route layers

## 6. Technical Design & Architecture

* **Task Model Class:** Implement a `Task` class to represent a task object with attributes and behavior.
* **Service Layer:** Introduce a `TaskService` class to handle business logic (add, retrieve, complete, delete tasks).
* **Dependency Injection:** Inject services into route handlers to improve testability and flexibility.
* **Modularization:** Separate business logic and data access from route files.
* **Blueprints:** Continue building with Flask Blueprints for routes.

##  Epic-Level Acceptance Criteria (Sprint 3)

* [ ] A `TaskService` class exists and is used by the API to handle all task operations.
* [ ] All route logic for tasks (`/api/tasks`) calls methods on the `TaskService` class (not procedural logic).
* [ ] Existing functionality (add, view, complete, delete) is fully supported using the new `TaskService`.
* [ ] The CLI is refactored to call the same `TaskService` class for manual testing.
* [ ] Manual CLI testing remains available for students to verify core logic.
* [ ] Automated API tests using the `requests` library are implemented and pass.
* [ ] All previously completed tasks are still functional and tested.
* [ ] A persistent storage interface (e.g., `load_tasks`, `save_tasks`) is defined in a way that can be swapped for a database.
* [ ] File storage remains the default, but logic is now ready for future DB substitution.


## 8. Risk Management

* **Refactor Complexity**: Risk of breaking working features during OOP refactor. *Mitigation:* Use TDD, refactor incrementally, and validate with tests.
* **Test Breakage**: Existing tests may fail due to interface changes. *Mitigation:* Update tests alongside implementation; maintain old behavior as needed.
  
## 9. Documentation Plan

* **README**: Add OOP and service explanations
* **API Documentation**: Review and update endpoint descriptions and structures
* **Design Docs**: Add `docs/architecture.md` to describe Task and Service classes
* **Test Plan/Test Cases**: Update based on new architecture
* **Sprint Report**: Document refactoring results and design improvements

## 10. Collaboration & Communication

* Use GitHub Project Board to track task progress
* Link issues to Key Tasks for visibility and tracking
* Create detailed pull request descriptions summarizing architecture changes
* Share CI build results and test coverage metrics with the team

## ✅ Sprint-Level Definition of Done (DoD)

Each User Story or Refactor is only considered **Done** when:

- [ ] All features implemented and tested
- [ ] Architecture updated to use `TaskService` and `TaskRepository`
- [ ] CLI feature (US029) supports marking tasks complete
- [ ] CLI writes changes to `tasks.json` via `TaskService`
- [ ] Automated tests using `requests` are created and pass (US035)
- [ ] Coverage remains ≥ 80%
- [ ] All updates committed with meaningful messages
- [ ] API Reference and README updated

## 📦 Sprint Deliverables

| Deliverable                      | Location                       |
| -------------------------------- | ------------------------------ |
| `TaskService` class              | `app/services/task_manager.py` |
| Updated API route logic          | `app/routes/tasks.py`          |
| CLI menu updated to use class    | `app/cli/cli_app.py`           |
| Persistent storage abstraction   | `app/services/task_storage.py` |
| Automated API tests (`requests`) | `tests/api/test_tasks_api.py`  |


📌 **Deprecation Notice**: The CLI will be deprecated in **Sprint 4**, once the Flask-based web UI is introduced. All future work will target web interaction and BDD/UI automation.



