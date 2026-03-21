from flask_restx import Namespace, fields

def register_user_schemas(ns: Namespace):
    """Register user-related schemas for API documentation"""
    # Schema with commong fields for both request and response    
    base_user_schema = ns.model('User', {
        'email': fields.String(required=True, description='The user email'),
        'name': fields.String(required=True, description='The user name'),
        'phone_number': fields.String(required=True, description='The user phone number'),
    })

    # Base user schema (for responses)
    user_response_schema = ns.inherit('UserResponse', base_user_schema, {
        'id': fields.String(readonly=True, description='The user ID (generated)'),
    })

    # Extend the user schema for creation (include password but remove id since it's generated)
    create_user_schema = ns.inherit('CreateUser', user_response_schema, { 
        'id': fields.String(readonly=True, required=False, description='The user ID (generated)'),
        'password': fields.String(required=True, description='The user password'),
    })

    return user_response_schema, create_user_schema