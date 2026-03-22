from http import HTTPStatus
from flask_restx import Namespace, Resource
from app.services.user import UserService
from app.api.v1.schemas.user import register_user_schemas
from app.utils.webhook import validate_webhook_signature

# Define the namespace for user-related operations
ns = Namespace('users', description='User module')

# Register user schemas for API documentation
user_response_schema, create_user_schema = register_user_schemas(ns)

# Initialize the user service
user_service = UserService()

@ns.route('/create')
class CreateUser(Resource):
    @ns.doc(params={"X-Hub-Signature-256": {"in": "header", "description": "HMAC signature for webhook validation", "required": True}})
    @ns.expect(create_user_schema, validate=True)
    @ns.marshal_with(user_response_schema, code=201, description='Retrieves the created user')
    @validate_webhook_signature()
    def post(self):
        # Get the user data from the request
        user_data = ns.payload
        
        # Create the user using the service
        user = user_service.create_user(user_data)

        # Return the created user and its serialized using the user_response_schema
        return user, HTTPStatus.CREATED