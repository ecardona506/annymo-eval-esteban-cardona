from flask_restx import Api
from app.api.v1.routes.user import ns as user

def register_v1(api: Api):
    """Register API namespaces for version 1."""
    api.add_namespace(user, path='/api/v1/user')