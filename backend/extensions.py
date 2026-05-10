from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()
login_manager = LoginManager()
cors = CORS()
