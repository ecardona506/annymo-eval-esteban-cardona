from app.models.user import User
from app.extensions import db
from flask_bcrypt import generate_password_hash
from app.exceptions.user import UserAlreadyExistsException

class UserService:
    @staticmethod
    def create_user(user_data: dict) -> User:
        """Create a new user and save to the database"""
        user = User(**user_data)
        user.password = UserService.hash_password(user)
        UserService.validate_user_creation(user)
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        return user
    
    @staticmethod
    def hash_password(user: User) -> str:
        """Hash the user's password"""
        return generate_password_hash(user.password).decode('utf-8')
    
    @staticmethod
    def validate_user_creation(user: User) -> None:
        """Validate user data before creation"""
        if UserService.get_user_by_email(user.email):
            raise UserAlreadyExistsException("User with the same email already exists")
        if UserService.get_user_by_phone_number(user.phone_number):
            raise UserAlreadyExistsException("User with the same phone number already exists")
    
    @staticmethod
    def get_user_by_email(email: str) -> User:
        """Retrieve a user by their email"""
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def get_user_by_phone_number(phone_number: str) -> User:
        """Retrieve a user by their phone number"""
        return User.query.filter_by(phone_number=phone_number).first()