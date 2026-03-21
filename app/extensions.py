from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions

# Database extension instance
db = SQLAlchemy()

# Migrate extension instance
migrate = Migrate()

# API extension instance
api_extension = Api(
    title="Annymo Eval REST API",
    version="1.0",
    description="REST API created as a solution to the first block of the technical test kit.",
    doc="/")