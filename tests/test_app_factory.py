# tests/test_app_factory.py
from app import create_app
from flask import Flask

def test_create_app_returns_flask_instance():
    """
    tc-us000-002: The create_app function should return a Flask app instance.
    """
    app = create_app()
    assert isinstance(app, Flask)

def test_app_returns_404_when_no_routes_defined():
    """
    tc-us000-003: When no routes are defined, the Flask app should return 404 for the index.
    """
    app = create_app()
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 404

def test_app_uses_db_repo():
    """
    TC-RF011-001: Flask App Loads with DB Injection
    Verifies that create_app() properly wires database repository and service
    """
    app = create_app()
    assert hasattr(app, "task_service")
    
    # Additional verification that it's a proper service
    assert app.task_service is not None
    assert hasattr(app.task_service, 'add_task')
    assert hasattr(app.task_service, 'get_tasks')
