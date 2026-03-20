from flask import Flask
from app.config import config_map
from app.extensions import db
from app.api.v1 import register_v1
from app.exceptions.handler import register_error_handlers
import os

def create_app() -> Flask:
    app = Flask(__name__)
    env = os.getenv("FLASK_ENV", "development")
    app.config.from_object(config_map[env])

    # Init extensions
    db.init_app(app)

    # Register namespaces for v1 API
    register_v1(app)

    # Register error handlers
    register_error_handlers(app)

    return app