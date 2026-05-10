from extensions import db
from datetime import datetime

class SharedTrip(db.Model):
    __tablename__ = 'shared_trips'
    
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    shared_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    share_token = db.Column(db.String(255), unique=True, nullable=False)
    is_public = db.Column(db.Boolean, default=True)
    likes = db.Column(db.Integer, default=0)
    view_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'shared_by': self.shared_by,
            'share_token': self.share_token,
            'is_public': self.is_public,
            'created_at': self.created_at.isoformat()
        }
