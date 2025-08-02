# app/__init__.py (Database-wired version)

from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.sqlalchemy_task import Base  # ✅ Correct import
from app.repositories.database_task_repository import DatabaseTaskRepository
from app.services.task_service import TaskService
from app.routes.tasks import tasks_bp
from app.routes.health import health_bp

def create_app(service=None):
    """
    Sprint 4: Database-wired Flask application
    """
    app = Flask(__name__)

    # 🔧 Database Setup (only if no service provided via dependency injection)
    if service is None:
        # Create SQLite database engine
        engine = create_engine("sqlite:///tasks.db")
        
        # Create session factory
        Session = sessionmaker(bind=engine)
        
        # Create database tables
        Base.metadata.create_all(engine)  # Creates tasks.db and tables
        
        # Wire up the repository and service
        repo = DatabaseTaskRepository(Session)
        service = TaskService(repo)
    
    # Inject the service into the app
    app.task_service = service

    # Register Blueprints
    app.register_blueprint(tasks_bp)
    app.register_blueprint(health_bp)

    # Global error handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad Request"}), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not Found"}), 404

    return app
