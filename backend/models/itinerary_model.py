from extensions import db

class ItineraryDay(db.Model):
    __tablename__ = 'itinerary_days'
    
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    day_number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date)
    notes = db.Column(db.Text)
    
    activities = db.relationship('ItineraryActivity', backref='day', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'day_number': self.day_number,
            'date': self.date.isoformat() if self.date else None,
            'notes': self.notes,
            'activities': [a.to_dict() for a in self.activities]
        }

class ItineraryActivity(db.Model):
    __tablename__ = 'itinerary_activities'
    
    id = db.Column(db.Integer, primary_key=True)
    day_id = db.Column(db.Integer, db.ForeignKey('itinerary_days.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    time_start = db.Column(db.Time)
    time_end = db.Column(db.Time)
    location = db.Column(db.String(255))
    estimated_cost = db.Column(db.Numeric(10, 2), default=0.00)
    activity_type = db.Column(db.Enum('adventure', 'sightseeing', 'food', 'nightlife', 'trekking', 'cultural', 'other'), default='other')

    def to_dict(self):
        return {
            'id': self.id,
            'day_id': self.day_id,
            'title': self.title,
            'description': self.description,
            'time_start': self.time_start.strftime('%H:%M') if self.time_start else None,
            'time_end': self.time_end.strftime('%H:%M') if self.time_end else None,
            'location': self.location,
            'estimated_cost': float(self.estimated_cost),
            'activity_type': self.activity_type
        }
