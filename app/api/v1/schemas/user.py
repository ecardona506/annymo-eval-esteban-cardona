from flask_restx import Namespace, fields

def register_user_schemas(ns: Namespace):
    """Register user-related schemas for API documentation"""
    # Base user schema (for responses)
    user_schema_dict = {
        'id': fields.String(required=True, description='The user ID'),
        'email': fields.String(required=True, description='The user email'),
        'username': fields.String(required=True, description='The user username'),
        'phone_number': fields.String(required=True, description='The user phone number'),
    }
    user_schema = ns.model('User', user_schema_dict)

    del user_schema_dict['id']  # Remove id from the creation schema since it's generated
    # Extend the user schema for creation (include password but remove id since it's generated)
    create_user_schema = ns.inherit('CreateUser', user_schema, { 
        'password': fields.String(required=True, description='The user password'),
    }) 

    return user_schema, create_user_schema