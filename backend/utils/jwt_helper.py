from flask_jwt_extended import create_access_token, create_refresh_token, decode_token
from datetime import timedelta

def generate_tokens(user_id):
    access_token = create_access_token(identity=str(user_id), expires_delta=timedelta(days=1))
    refresh_token = create_refresh_token(identity=str(user_id), expires_delta=timedelta(days=30))
    return access_token, refresh_token
