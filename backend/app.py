from flask import Flask, render_template
from config import Config
from extensions import db, jwt, login_manager, cors
import os

# Import models to ensure they are registered
from models.user_model import User
from models.trip_model import Trip
from models.destination_model import Destination
from models.itinerary_model import ItineraryDay, ItineraryActivity
from models.expense_model import Expense
from models.packing_model import PackingList
from models.notes_model import Note
from models.shared_trip_model import SharedTrip
from models.activity_model import Activity
from models.notification_model import Notification
from models.admin_model import AdminUser, AdminLog
from models.settings_model import UserSetting
from models.analytics_model import Analytics, DestinationAnalytics
from models.report_model import Report

def create_app(config_class=Config):
    app = Flask(__name__, 
                static_folder='../frontend/static', 
                template_folder='../frontend/templates')
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    cors.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints (to be created)
    from routes.auth_routes import auth_bp
    from routes.dashboard_routes import dashboard_bp
    from routes.admin_routes import admin_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    @app.route('/')
    def index():
        return render_template('auth/login.html')

    with app.app_context():
        db.create_all() 
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
