from http import HTTPStatus
from flask_restx import Namespace, Resource, reqparse
from app.services.user import UserService
from app.api.v1.schemas.user import register_user_schemas
from app.utils.webhook import validate_webhook_signature

# Define the namespace for user-related operations
ns = Namespace('users', description='User module')

# Register user schemas for API documentation
user_response_schema, create_user_schema, users_list_schema = register_user_schemas(ns)

# Initialize the user service
user_service = UserService()

# Parser for list users query parameters
list_users_parser = reqparse.RequestParser()
list_users_parser.add_argument('page', type=int, default=1, help='Page number (default: 1)')
list_users_parser.add_argument('per_page', type=int, default=10, help='Items per page (default: 10)')

@ns.route('/all')
class AllUsers(Resource):
    @ns.doc('list_users')
    @ns.expect(list_users_parser)
    @ns.marshal_with(users_list_schema, code=200, description='List of users with pagination')
    def get(self):
        args = list_users_parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        
        result = user_service.get_all_users(page=page, per_page=per_page)
        
        return {
            'users': result['users'],
            'pagination': {
                'page': result['page'],
                'per_page': result['per_page'],
                'total': result['total'],
                'pages': result['pages']
            }
        }, HTTPStatus.OK

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