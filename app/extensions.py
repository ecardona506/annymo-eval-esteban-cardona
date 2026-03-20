from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

# Initialize extensions

# Database instance
db = SQLAlchemy()

# API instance
api = Api(
    title="Annymo Eval REST API",
    version="1.0",
    description="REST API created as a solution to the first block of the technical test kit.",
    doc="/")