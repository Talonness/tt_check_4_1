# app/main.py
from app import create_app

app = create_app()

if __name__ == "__main__":
    import os
    # Use environment variable to control debug/reload for CI
    testing = os.getenv('TESTING', '').lower() == 'true'
    app.run(
        debug=not testing,  # Disable debug in CI
        use_reloader=not testing  # Disable reloader in CI
    )