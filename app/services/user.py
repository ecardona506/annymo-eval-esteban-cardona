from app.models.user import User
from app.extensions import db
from flask_bcrypt import generate_password_hash

class UserService:
    @staticmethod
    def create_user(user_data: dict) -> User:
        """Create a new user and save to the database"""
        user = User(**user_data)
        user.password = UserService.hash_password(user)
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