# ✅ Task Tracker – Full User Story Backlog

## User Stories

<!-- Sprint: 1 -->
* **US000 – Initial Setup & Validation**: 👤 Individual Project
 “As a developer, I want to validate the development environment and project scaffolding so I can begin development with confidence.”
🧑‍💻 **Owner:** Dev
🗓️ **Sprint:** 1
📌 **Status:** Complete
📝 Notes:
This user story ensures your local dev environment, GitHub setup, and virtual environment are working. It mirrors the real-world “first commit” milestone in full-stack teams. It also introduces pytest and lays the groundwork for test-driven development (TDD).

<!-- Sprint: 1 -->
* **US001 – Health Check Endpoint**: 👤 Individual Project
 “As a developer or QA engineer, I want a /api/health endpoint that returns system status in JSON, and I want this tested automatically using GitHub Actions, so I can ensure the server is running and verify tests on every push.”
🧑‍💻 **Owner:** Dev
🗓️ **Sprint:** 1
📌 **Status:** Complete
📝 Notes:
This story introduces your first API route and automates testing via GitHub Actions CI. It’s a realistic real-world feature that supports monitoring and validates that infrastructure is running — a first step in DevOps pipelines.

<!-- Sprint: 1 -->
* **US002 – Add Task via API**: 👤 Individual Project
 “As a user, I want to add a new task with a description to my to-do list so I can track tasks. If I forget to enter a task name, I should receive an error so I don’t create empty tasks.”
🧑‍💻 **Owner:** Dev
🗓️ **Sprint:** 1
📌 **Status:** Complete
📝 Notes:
This introduces your first POST route and begins enforcing data validation with meaningful API responses. You will use both pytest and manual tools (curl/Postman) to test input validation and persistence. Forms the basis for all future task logic.

<!-- Sprint: 1 -->
* **US003 – View Tasks (List)**: 👤 Individual Project
 “As a user, I want to view a list of all my tasks so that I can see each task’s status.”
🧑‍💻 **Owner:** Dev
🗓️ **Sprint:** 1
📌 **Status:** Complete
📝 Notes:
Introduces your first GET route and begins the idea of “system state.” You will test both empty and populated task states. This also lays the foundation for understanding JSON structure and return codes for frontend use later.

<!-- Sprint: 1 -->
* **US004 - Add Task via CLI (stub)**👤 Individual Project
 “As a user, I want to add a task using the command line so I can interact with the app without using the browser or Postman.”
🧑‍💻 **Owner:** Dev
🗓️ **Sprint:** 1
📌 **Status:** Complete
📝 Notes:
This CLI stub provides a simple manual way to test task creation logic and persistence before the UI exists. It emphasizes separation of concerns — the CLI calls the core logic but does not own it. Will be deprecated in favor of Web UI later.

<!-- Sprint: 2 -->
* **US005 – Mark Task Complete**: 👤 Individual Project
“As a user, I want to mark a task as completed so I can focus on remaining tasks.”
🧑‍💻 **Owner:** Dev
🗓️ **Sprint:** 2
📌 **Status:** Complete

* **US006 - CLI UI: Add**: 👤 Individual Project
“As a user, I want to add a task using the CLI, so I can manually test the logic and persistence before transitioning to the web UI.”
🧑‍💻 **Owner:** Dev
🗓️ **Sprint:** 2
📌 **Status:** Complete

🚀 The CLI UI is intended as an interim manual testing tool and learning aid. It will help validate logic before web UI and Selenium/Playwright automation are introduced in Sprint 4.

<!-- Sprint: 2 -->
* **US007 – Remove Task**: 👤 Individual Project
“As a user, I want to delete a task from my list to keep it up to date.”
🧑‍💻 **Owner:** Dev
🗓️ **Sprint:** 2
📌 **Status:** Complete

<!-- NOT PLANNED -->
* **US008 – Tag Tasks (Assign Category)**: “As a user, I want to assign category tags to each task (e.g., "work", "personal") when creating or editing tasks so I can organize my task list.”
👥 Group: Available for Group Project

<!-- NOT PLANNED -->
* **US009 – Edit Task Title**: “As a user, I want to edit a task’s Title so I can correct or update information.”
👥 Group: Available for Group Project

<!-- NOT PLANNED -->
* **US010 – Assign Due Date**: “As a user, I want to assign a due date to each task so I can track deadlines.”
👥 Group: Available for Group Project

<!-- Sprint: 2 -->
* **US011 – Persist Tasks**: 👤 Individual Project
“As a user, I want tasks saved between sessions so I don’t lose my list.”
🧑‍💻 **Owner:** Dev
🗓️ **Sprint:** 2
📌 **Status:** Complete

<!-- NOT PLANNED -->
* **US012 – User Login**: “As a user, I want to log in with a username/password to access my dashboard.”
👥 Group: Available for Group Project

<!-- NOT PLANNED -->
* **US013 – Search Tasks**: “As a user, I want to search tasks by keyword.”
👥 Group: Available for Group Project

<!-- Sprint: 4 -->
* **US014 – Add UI for Task Creation**: 👤 Individual Project
“As a user, I want to use a web form to create tasks”
🧑‍💻 **Owner:** Frontend/Dev
🗓️ **Sprint:** 4
📌 **Status:** Planned

<!-- Sprint: 2 -->
* **US015 – API Error Handling**: 👤 Individual Project
“API (RESPONSE), Error Handling, TDD, Global”
🧑‍💻 **Owner:** Dev
🗓️ **Sprint:** 2
📌 **Status:** Complete

<!-- NOT PLANNED -->
* **US016 – Filter Tasks by Status**: “As a user, I want to filter tasks by complete/incomplete.”
👥 Group: Available for Group Project

<!-- NOT PLANNED -->
* **US017 – Responsive UI**: “As a user, I want the task list to look good on mobile.”
👥 Group: Available for Group Project

<!-- Sprint: 4 -->
* **US018 – View Task List (UI)**: 👤 Individual Project
“As a user, I want to see a table of tasks in the browser.”
🧑‍💻 **Owner:** Frontend/Dev
🗓️ **Sprint:** 4
📌 **Status:** Planned

<!-- NOT PLANNED -->
* **US019 – Add Tags to Tasks**: “As a user, I want to tag tasks with categories.”
👥 Group: Available for Group Project

<!-- NOT PLANNED -->
* **US020 – User Registration**: “As a new user, I want to register with a username/password to create an account.”
👥 Group: Available for Group Project

<!-- NOT PLANNED -->
* **US021 – Secure Session Management**: “As a logged-in user, I want my session to persist securely.”
👥 Group: Available for Group Project

<!-- NOT PLANNED -->
* **US022 – User Logout**: “As a logged-in user, I want to log out and terminate my session.”
👥 Group: Available for Group Project

<!-- NOT PLANNED -->
* **US023 – Password Validation & Errors**: “As a user, I want clear messages if login or registration fails.”
👥 Group: Available for Group Project

<!-- NOT PLANNED -->
* **US024 – Filter Tasks by Tag**: “As a user, I want to filter tasks by tag so I can quickly view only relevant items.”
👥 Group: Available for Group Project

<!-- NOT PLANNED -->
* **US025 – Overdue Task Alerts**: “As a user, I want the system to highlight or notify me when a task is overdue so I don’t miss important tasks.”
👥 Group: Available for Group Project

<!-- Sprint: 4 -->
* **US026 – Task Menu UI**: 👤 Individual Project “As a user, I want a menu on the web page that lets me navigate to add, edit, delete, complete, and view tasks, so I can easily access all core features from one place”
🧑‍💻 **Owner:** Frontend/Dev
🗓️ **Sprint:** 4
📌 **Status:** Planned

<!-- Sprint: 4 -->
* **US027 – View Task Report**: 👤 Individual Project “As a user, I want to see a report of all tasks from the command line.”
🧑‍💻 **Owner:** Dev
🗓️ **Sprint:** 1
📌 **Status:** Completed

<!-- Sprint: 1 -->
* **US028 - CLI Menu UI**: 👤 Individual Project “As a user, I want to view, add and quit tasks in the CLI, so I can verify stored data and check task completion status.”
🧑‍💻 **Owner:** Dev
🗓️ **Sprint:** 1
📌 **Status:** Completed

<!-- Sprint 3 -->
* **US029 - CLI UI: Mark Task Complete**: 👤 Individual Project. “As a user, I want to mark a task as complete via CLI, so I can validate completion manually.”
🧑‍💻 **Owner:** Backend/CLI Dev
🗓️ **Sprint:** 3
📌 **Status:** Planned

<!-- NOT PLANNED -->
* **US030 - CLI UI: Delete Task**: As a user, I want to delete task as via CLI, so I can validate deletion manually. 
👥 Group: Available for Group Project

<!-- Sprint: 4 -->
* **US031 - Show Current Time via External API**: 👤 Individual Project.  “As a user,
I want to view the current time for my selected timezone,
So I can track tasks across different regions or validate time-based info.”
🧑‍💻 **Owner:** Dev
🗓️ **Sprint:** 4
📌 **Status:** Planned
🔁 Notes:
  * Requires integration with a public API (e.g., WorldTimeAPI.org)
  * May be displayed via Web UI or used internally (e.g., for timestamping or validation)
  * Can help introduce mocking external APIs during testing

<!-- Sprint: 4 -->
* **US032 – BDD Test: Task Creation via Web UI**: 👤 Individual Project “As a QA engineer, I want to define behavior-driven tests for task creation via the browser so I can verify user-facing features with natural language specifications.“
🧪 **Owner:** QA
🗓️ **Sprint:** 4
📌 **Status:** Planned
🔁 Notes: Robot Framework or Behave using Gherkin syntax.

<!-- Sprint: 4 -->
* **US033 – User Journey: Manual Task Workflow**: 👤 Individual Project “As a user, I want to manually complete a full task workflow so I can validate that the app supports typical task management “behavior.
🧍 **Owner:** User
🗓️ **Sprint:** 4
📌 **Status:** Planned
🔁 Notes: Applies to either CLI (Sprint 3) or Web UI (Sprint 4)

<!-- Sprint: 4 -->
* ***US034 – CI Automation for Task Features**: 👤 Individual Project “As a DevOps or QA engineer, I want all automated tests to run in CI so I can catch errors or regressions before release.“
🧪 **Owner:** QA
🗓️ **Sprint:** 4
📌 **Status:** Planned
🔁 Notes: Builds on GitHub Actions CI pipeline, includes all testing types

<!--Sprint:3 -->
* ***US035 - API Testing Automation (requests)**: 👤 Individual Project “As a QA engineer, I want to write automated API tests using the requests library so I can verify endpoint behavior without manual tools.“
🧪 **Owner:** QA
🗓️ **Sprint:** 3
📌 **Status:** Planned
🔁 Notes: Replaces or complements Postman and curl tests


## ✅ Acceptance Criteria

* **US000 – Initial Setup & Validation**: 
  * [ ] Project can be cloned and run locally using `python3 -m flask run`
  * [ ] Virtual environment is created and dependencies are managed with `requirements.txt`
  * [ ] Directory structure is scaffolded (e.g., `app/`, `tests/`)
  * [ ] GitHub repository includes `.gitignore`, LICENSE, and README
  * [ ] Initial commit is pushed to `main`
* **US001 – Health Check Endpoint**:
  * [ ] `GET /api/health` returns `{ "status": "OK" }`
  * [ ] Response includes HTTP 200 status code
  * [ ] Endpoint has automated test using `pytest`
  * [ ] CI is configured to run the test on every push to `main` 
* **US002 – Add Task via API**: 
  * [ ] `POST /api/tasks` accepts a JSON body with a task title
  * [ ] Task is added to an in-memory list or temporary storage
  * [ ] Title field is required; request fails with a 400 error if missing or empty
  * [ ] Valid requests return 201 and include the new task in JSON
  * [ ] All logic is covered by unit tests
* **US003 – View Tasks (List)**: 
  * [ ] `GET /api/tasks` returns a JSON array of all tasks
  * [ ] Each task includes `id`, `title`, and `completed` status
  * [ ] Endpoint returns 200 with correct structure even when task list is empty
  * [ ] Tests validate response structure and content
* **US004 - Add Task via CLI (stub)**
  * [ ] Prompt for task title and description
  * [ ] Add task to in-memory list (Sprint 1 only)
  * [ ] Display confirmation message 
* **US005 – Mark Task Complete**:
  * [ ] A completed task’s `completed` field is set to `true`.
  * [ ] `PUT /api/tasks/<id>` marks the specified task complete.
  * [ ] Invalid task IDs return a 404 error.
  * [ ] Changes are saved to `data/tasks.json`.
  * [ ] Unit tests cover valid and invalid use cases.
* **US006 - CLI UI: Add Task**: 
  * [ ] User can enter a task title and optional description via CLI prompt.
  * [ ] Task is saved in memory or persisted to file (if enabled).
  * [ ] CLI confirms success with a message and task ID.
  * [ ] Errors are shown if input is invalid (e.g., blank title).
  * Store and read tasks from JSON file
* **US007 – Remove Task**:
  * [ ] `DELETE /api/tasks/<id>` deletes the specified task.
  * [ ] Nonexistent task IDs return 404.
  * [ ] Deleted tasks no longer appear in the list.
  * [ ] Changes are saved to `data/tasks.json`.
  * [ ] Unit tests cover valid and invalid deletions.
 
* **US011 – Persist Tasks**:
  * [ ] Tasks are saved to a file (`data/tasks.json`).
  * [ ] Tasks are loaded from the file on app startup.
  * [ ] Adding, editing, or deleting a task updates the file.
  * [ ] File is formatted as a valid JSON array.
  * [ ] Functionality is covered by integration tests. 

* **US014 – Add UI for Task Creation**: 
  * [ ] Create a simple HTML form for task creation (title and description).
  * [ ] Submitting the form with valid input sends a POST request to /api/tasks.
  * [ ] The form handles and displays error messages when title is missing.
  * [ ] On success, the new task is visible in the updated list or a success message is shown.
  * [ ] UI is tested using Selenium or Playwright to verify valid and invalid input handling.
  
* **US015 – API Error Handling**:
  * [ ] Create a global error handler using `@app.errorhandler`
  * [ ] All 400, 404, and 500 errors return a JSON body like `{ "error": "Message here" }`
  * [ ] Errors are logged or printed for debugging
  * [ ] Tests verify that error format is consistent for expected error cases

* **US018 – View Task List/Report (UI)**: 
  * [ ] Tasks are rendered in a table format in the browser
  * [ ] Each task displays: Title, Description, and Completion Status
  * [ ] Completed tasks are visually distinguishable (e.g., checkbox, strikethrough, or ✅)
  * [ ] The page updates when tasks are added, modified, or deleted
  * [ ] The table is rendered using Jinja2 and Flask templates
  * [ ] The UI gracefully handles empty task lists (e.g., shows “No tasks yet.”)
  * [ ] Manual testing confirms task list matches data in JSON file
  * [ ] Automated UI tests (Selenium/Playwright) validate expected rendering

* **US026 – Task Menu UI**:
  * [ ] A navigation menu is displayed with links to: Add Task, View Tasks, and Reports.
  * [ ] Menu clearly indicates which section is active (e.g., highlight, underline).
  * [ ] Navigation works across views/pages without breaking functionality.
  * [ ] Menu is responsive and accessible (keyboard-friendly, screen-reader-friendly).
  * [ ] Selenium or Playwright test validates clickable navigation between sections. 
  
* **US027 – View Task Report**: 
  * [ ] CLI allows user to enter tasks using input()
  * [ ] CLI displays all added tasks (title + description)
  * [ ] User can quit from CLI
  * [ ] Tasks persist in memory during CLI session
  * [ ] Code structured to allow future refactor to class-based CLI (Sprint 3)
  * [ ] UI and CLI versions are both tested to verify correct calculation from persisted data.

* **US028 - Extend CLI View Tasks**:
  * [ ] CLI displays all stored tasks with their id, title, description, and completed status.
  * [ ] Output is readable and presented in a list format.
  * [ ] If no tasks exist, a suitable message is shown.

* **US029 - CLI UI:Mark Task Complete**
  * [ ] A user can select a task by ID from the CLI and mark it as completed.
  * [ ] CLI provides visual confirmation when a task is marked complete.
  * [ ] If a non-existent ID is entered, an error message is shown: "Task not found."
  *[ ] If no tasks exist, the CLI shows a helpful message: "No tasks available to complete."
  * [ ] The updated task state is saved in the JSON file (completed: true).
  * [ ] Marked tasks remain visible in the list with a visual cue like [X] or ✔.
  * [ ] All state changes are persisted and visible across CLI and API views.
  * [ ] CLI supports marking multiple tasks in sequence without restarting the app.
  * [ ] Automated CLI tests verify:
    * Marking a valid task as complete updates JSON correctly.
    * Invalid or missing task ID triggers appropriate error.
  * [ ] Manual testing checklist updated (if applicable).

* **US031 - Show Current Time via External API**
  * [ ] A new route /api/time returns the current time as JSON
  * [ ] Uses a requests.get() call to fetch time from an external API
  * [ ] Handles network errors or invalid responses gracefully
  * [ ] Unit test uses mocking to simulate external API response
  * [ ] Optional: Display current time on the Web UI via a dedicated section

* **US032 - BDD Test: Task Creation via Web UI**
  * [ ] Write a `.feature` file with at least one Gherkin scenario for task creation
  * [ ] Include scenarios for both valid and invalid input
  * [ ] Implement step definitions to automate tests via Robot Framework or Behave
  * [ ] Test results are visible in CI or saved as a report
  * [ ] All steps are aligned with UI behavior and verified manually beforehand

* **US032 - User Journey: Manual Task Workflow**
  * [ ] Manually add a task (via CLI or Web UI)
  * [ ] Manually view task list
  * [ ] Mark a task as complete
  * [ ] Delete a task
  * [ ] After each step, validate changes in the UI and in persistent storage (file or DB)
  * [ ] Submit screenshots or logs as evidence of the journey

* **US034 - CI Automation for Task Features**
  * [ ] Run unit tests (pytest) with test coverage report
  * [ ] Run API tests using requests or Postman collection
  * [ ] Run UI tests using Selenium or Playwright
  * [ ] Run BDD acceptance tests via Robot Framework or Behave
  * [ ] Ensure all stages run in GitHub Actions and fail if any test fails

* **US035 - API Testing Automation (requests)**
  * [ ] Write test scripts using requests to test core API routes
  * [ ] Cover at least: POST /api/tasks, GET /api/tasks, PUT /api/tasks/<id>, DELETE /api/tasks/<id>
  * [ ] Include both positive and negative test cases
  * [ ] Save scripts in /tests/api/ and integrate with pytest
  * [ ] Document how to run and interpret the results