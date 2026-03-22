from flask import Flask
from app.config import config_map
from app.extensions import db, api_extension, migrate   
from app.api.v1 import register_v1
from app.exceptions.handler import register_error_handlers
import os

def create_app() -> Flask:
    app = Flask(__name__)
    env = os.getenv("FLASK_ENV", "development")
    app.config.from_object(config_map[env])

    # Init extensions
    db.init_app(app)

    # Initialize Flask-Migrateate with the Flask app and SQLAlchemy database
    migrate.init_app(app, db)

    # Register namespaces for v1 API
    api_extension.init_app(app)
    register_v1(api_extension)

    # Register error handlers
    register_error_handlers(app)

    return app