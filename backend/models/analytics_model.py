from extensions import db
from datetime import datetime

class Analytics(db.Model):
    __tablename__ = 'analytics'
    
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(50), nullable=False) # e.g., 'trip_created', 'user_signup'
    event_data = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def log_event(event_type, event_data=None, user_id=None):
        event = Analytics(event_type=event_type, event_data=event_data, user_id=user_id)
        db.session.add(event)
        db.session.commit()

class DestinationAnalytics(db.Model):
    __tablename__ = 'destination_analytics'
    
    id = db.Column(db.Integer, primary_key=True)
    destination_name = db.Column(db.String(100), nullable=False)
    search_count = db.Column(db.Integer, default=0)
    trip_count = db.Column(db.Integer, default=0)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
