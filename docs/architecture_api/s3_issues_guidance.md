# 🏁 Sprint 3 Issue Guidance

## Parent Issue Sprint 3 Completion
* *Description:*
  
  This sprint focuses on refactoring the codebase to introduce object-oriented design, injecting persistence services, and laying the groundwork for future extensibility and database support. No new user-facing features are added in this sprint, but existing functionality is restructured for maintainability and testability.

  - ✅ Epic-Level Acceptance Criteria (Sprint 3)

  * [ ] A `TaskManager` class exists and is used by the API to handle all task operations.
  * [ ] All route logic for tasks (`/api/tasks`) calls methods on the `TaskManager` class (not procedural logic).
  * [ ] Existing functionality (add, view, complete, delete) is fully supported using the new `TaskManager`.
  * [ ] The CLI is refactored to call the same `TaskManager` class for manual testing.
  * [ ] Manual CLI testing remains available for students to verify core logic.
  * [ ] Automated API tests using the `requests` library are implemented and pass.
  * [ ] All previously completed tasks are still functional and tested.
  * [ ] A persistent storage interface (e.g., `load_tasks`, `save_tasks`) is defined in a way that can be swapped for a database.
  * [ ] File storage remains the default, but logic is now ready for future DB substitution.

  - ✅ Definition of Done (applies to each user story or task)

    Each User Story or Refactor is only considered **Done** when:

    * [ ] Unit tests exist for all methods in `TaskManager`.
    * [ ] Pytest test suite passes (`pytest -v`)
    * [ ] Code is committed and pushed to GitHub.
    * [ ] Any external test scripts using `requests` are placed in `tests/api/`.
    * [ ] Code passes linting and follows documented naming/style conventions.
    * [ ] Acceptance Criteria for the User Story are fulfilled.
    * [ ] All routes call `TaskManager`, not direct file access.
    * [ ] The CLI uses `TaskManager` only and functions for manual verification.
    * [ ] JSON file I/O is abstracted for future DB integration.
    * [ ] Code is committed and pushed to GitHub with updated documentation.

  - 📂 Sprint 2 Tracked User Stories (Sub-Issues)

    * **US011 – Persist Tasks**: Already implemented (Sprint 2, supports refactor)
    * **US027 – View Task Report (CLI)**: Supports CLI-to-UI migration in Sprint 4
    * **US028 – CLI Logic (Add/View/Quit)**: Fully implemented
    * **US029 – CLI UI: Mark Task Complete**
    * **US035 – API Testing Automation (requests)**
  

  - 📂 Sprint 3 Refactor Tasks (Sub-Issues)

    * [ ] #RF003 – Refactor: Create `Task` class with fields and methods
    * [ ] #RF004 – Refactor: Create `TaskService` class to manage task logic
    * [ ] #RF005 – Refactor: Create `FileStorage` service to abstract file operations
    * [ ] #RF006 – Refactor: Inject `TaskService` into route handlers using app context
    * [ ] #RF007 – Regression Testing: Verify all prior endpoints (Add, View, Edit, Delete, Complete) still work after refactor


  - 🔧 Sprint-Level Technical Tasks (Sub-Issues)

    * [ ] ARCH001 – Add class diagram to `docs/architecture.md` and explain key design choices
    * [ ] #DOC004 – Update API documentation to reflect injected services
    * [ ] #TEST004 – Write unit tests for `Task`, `TaskService`, and `FileStorage`
    * [ ] #TEST005 – Run regression tests to validate endpoint behavior post-refactor
    * [ ] #DB001 – Draft ERD for Sprint 4 and commit to `docs/sprint4_erd.md`
    * [ ] #COV003 – Add coverage badge for API layer
      * Configure `pytest-cov` to track coverage of `routes/` and `services/`
      * Generate `.coverage` and `coverage.xml` reports
      * Upload to Codecov or Coveralls via GitHub Actions
      * Add markdown badge to top of `README.md`
  

  - 📁 Related Documentation

    * `docs/api_documentation.md`
    * `docs/test_plan.md`
    * `docs/test_cases.md`
    * `docs/architecture.md`
    * `docs/sprint4_erd.md`
    * `README.md`

---
## 🔧 Detailed Sub-Issues

1. 🎯 *Title:* **US007 – Edit Task**
     - *Description:* 
      
       As a user, I want to edit a task’s title so I can fix mistakes or update descriptions.
       - ✅ Acceptance Criteria
           - [ ] `PUT /api/tasks/<id>` allows updating the title of an existing task.
           - [ ] Empty or missing title returns a 400 error.
           - [ ] Nonexistent IDs return 404.
           - [ ] Changes persist in `data/tasks.json`.
           - [ ] Endpoint is tested for success and error cases.

       - 📌 Sub-Issues of **US005 – Remove Task**
           - [ ] Implement `PUT /api/tasks/<id>` title update logic
           - [ ] Validate title input
           - [ ] Handle 400 and 404 cases
           - [ ] Write unit tests
           - [ ] Update API docs with example payload


2. 🎯 **RF003 – Refactor: Convert Tasks to Task Class**

* *Description:*
  
  Refactor task dictionaries into a `Task` class to support future features like timestamps, categorization, and encapsulated behavior.

  * ✅ **Acceptance Criteria**

    * [ ] `Task` class is defined in `models/task.py` with attributes `id`, `title`, `completed`
    * [ ] `__init__`, `to_dict()`, and `from_dict()` methods implemented
    * [ ] Routes/functions refactored to use `Task` instances instead of raw dicts
    * [ ] Unit tests validate object conversion and behavior
    * [ ] All previous tests continue to pass after migration

  * 📌 **Sub-Issues of RF003**

    * [ ] Create `models/task.py` with `Task` class and methods
    * [ ] Refactor route logic to use Task instances
    * [ ] Update storage helpers to read/write `Task` objects as JSON
    * [ ] Write unit tests for `to_dict()` and `from_dict()`
    * [ ] Confirm compatibility with all previous endpoints

---

3. 🎯 **RF004 – Refactor: Move Task Logic into Service Layer**
* *Description:*
  
    Introduce a `TaskService` layer to handle business logic like adding, editing, or deleting tasks, improving separation of concerns.

    * ✅ **Acceptance Criteria**

        * [ ] New module `services/task_service.py` exists
        * [ ] All core task operations are implemented in service methods
        * [ ] Routes call service methods instead of handling logic directly
        * [ ] Unit tests verify service logic independently
        * [ ] Existing endpoint behavior remains unchanged

    * 📌 **Sub-Issues of RF004**

        * [ ] Create `services/task_service.py` and define core functions (add, update, delete)
        * [ ] Refactor routes to use these functions
        * [ ] Add test coverage for service methods
        * [ ] Update documentation/comments to reflect architectural layers

---

4. 🎯 **RF005 – Refactor: Inject Storage Layer (DI for Testing)**
* *Description:*
  
  Refactor the app to use dependency injection for the storage layer so it can be swapped (e.g., memory vs. file) for easier testing and extensibility.

    * ✅ **Acceptance Criteria**

      * [ ] Define an abstract `Storage` interface (e.g., `read_tasks()`, `write_tasks()`)
      * [ ] Inject storage implementation into services or routes
      * [ ] Create test implementation (in-memory or mock)
      * [ ] Update `create_app()` to configure correct storage backend
      * [ ] All tests run using injected storage

    * 📌 **Sub-Issues of RF005**

      * [ ] Define `Storage` interface or base class
      * [ ] Implement file and mock/in-memory storage
      * [ ] Update services to use injected storage
      * [ ] Modify `create_app()` for configurable backend
      * [ ] Add tests using mock storage

---

5. 🎯 **RF006 – Refactor: Modularize Test Files**

* *Description:*
  
  Break up monolithic test files into logically organized test modules by route or feature, ensuring each test file maps to a functional unit.

  * ✅ **Acceptance Criteria**

    * [ ] Test files are split and stored in `tests/tasks/` (e.g., `test_add_task.py`, `test_complete_task.py`)
    * [ ] Each file includes grouped related test cases
    * [ ] Tests use fixtures and shared setup logic for reusability
    * [ ] `pytest` runs all tests without warnings or errors
    * [ ] Coverage remains ≥ prior sprint

  * 📌 **Sub-Issues of RF006**

    * [ ] Create modular test files and organize by feature
    * [ ] Use fixtures for test client and sample task data
    * [ ] Migrate test logic from old files
    * [ ] Confirm all tests run and coverage is maintained
    * [ ] Update `README.md` with new test structure

---

6. 🎯 **RF007 – Refactor: Add Blueprint for API Health & Metadata**

   * *Description:*
     
     Move the health check and future meta endpoints (like `/version`, `/info`) into a separate `routes/meta.py` blueprint for separation from task routes.

     * ✅ **Acceptance Criteria**

       * [ ] Create `routes/meta.py` and register as a blueprint
       * [ ] Move `/api/health` to `routes/meta.py`
       * [ ] Confirm `/api/health` behavior and test coverage remain unchanged
       * [ ] Route structure is organized and modular
       * [ ] Blueprint is documented and visible in app structure

     * 📌 **Sub-Issues of RF007**

       * [ ] Create `routes/meta.py` and move health route
       * [ ] Register new blueprint in `create_app()`
       * [ ] Refactor test file for health endpoint
       * [ ] Update API documentation to reflect file change

7. **US035 - API Testing Automation (requests)

  * [ ] Organize tests into `tests/api/`
  * [ ] Write request-based test functions for:
      - POST /api/tasks
      - GET /api/tasks
      - PUT /api/tasks/<id>
      - DELETE /api/tasks/<id>
  * [ ] Include tests for expected status codes and error messages
  * [ ] Document how to run these tests in `README.md` or `docs/test_plan.md`
