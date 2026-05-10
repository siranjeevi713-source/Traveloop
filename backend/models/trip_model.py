from extensions import db
from datetime import datetime

class Trip(db.Model):
    __tablename__ = 'trips'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    cover_image = db.Column(db.String(255))
    status = db.Column(db.Enum('upcoming', 'completed', 'draft'), default='draft')
    trip_type = db.Column(db.String(50), default='Solo') # 'Adventure', 'Family', 'Solo', 'Luxury', 'Business'
    budget_limit = db.Column(db.Numeric(10, 2), default=0.00)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    destinations = db.relationship('Destination', backref='trip', lazy=True, cascade="all, delete-orphan")
    itinerary_days = db.relationship('ItineraryDay', backref='trip', lazy=True, cascade="all, delete-orphan")
    expenses = db.relationship('Expense', backref='trip', lazy=True, cascade="all, delete-orphan")
    packing_items = db.relationship('PackingList', backref='trip', lazy=True, cascade="all, delete-orphan")
    shared_details = db.relationship('SharedTrip', backref='trip', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'cover_image': self.cover_image,
            'status': self.status,
            'trip_type': self.trip_type,
            'budget_limit': float(self.budget_limit),
            'created_at': self.created_at.isoformat()
        }
