from models.user_model import User
from extensions import db
from utils.jwt_helper import generate_tokens

class AuthService:
    @staticmethod
    def register_user(data):
        if User.query.filter_by(email=data['email']).first():
            return None, "Email already exists"
        
        user = User(
            full_name=data['full_name'],
            email=data['email']
        )
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return user, "User registered successfully"

    @staticmethod
    def authenticate_user(email, password):
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            access_token, refresh_token = generate_tokens(user.id)
            return {
                "user": user.to_dict(),
                "access_token": access_token,
                "refresh_token": refresh_token
            }, "Login successful"
        return None, "Invalid email or password"
