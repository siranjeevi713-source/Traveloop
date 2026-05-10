import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from app import create_app
from extensions import db
from models.admin_model import AdminUser
from models.analytics_model import DestinationAnalytics

app = create_app()

with app.app_context():
    # Create tables
    db.drop_all()
    db.create_all()
    
    # Add default admin if not exists
    if not AdminUser.query.filter_by(email='admin@traveloop.com').first():
        admin = AdminUser(username='admin', email='admin@traveloop.com')
        admin.set_password('admin123')
        db.session.add(admin)
        print("Default admin created: admin@traveloop.com / admin123")
    
    from models.user_model import User
    if not User.query.filter_by(email='test@example.com').first():
        user = User(full_name='Test Explorer', email='test@example.com')
        user.set_password('password123')
        db.session.add(user)
        print("Default user created: test@example.com / password123")
    
    # Add some dummy analytics data
    if not DestinationAnalytics.query.first():
        dests = [
            DestinationAnalytics(destination_name='Bali, Indonesia', trip_count=156),
            DestinationAnalytics(destination_name='Switzerland', trip_count=98),
            DestinationAnalytics(destination_name='Thailand', trip_count=245),
            DestinationAnalytics(destination_name='Kerala, India', trip_count=187),
            DestinationAnalytics(destination_name='Dubai, UAE', trip_count=134)
        ]
        db.session.add_all(dests)
        print("Dummy analytics data added")
    
    db.session.commit()
    print("Database setup complete")
