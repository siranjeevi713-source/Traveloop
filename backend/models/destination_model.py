from extensions import db

class Destination(db.Model):
    __tablename__ = 'destinations'
    
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100))
    order_index = db.Column(db.Integer, default=0)
    arrival_date = db.Column(db.Date)
    departure_date = db.Column(db.Date)

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'name': self.name,
            'country': self.country,
            'order_index': self.order_index,
            'arrival_date': self.arrival_date.isoformat() if self.arrival_date else None,
            'departure_date': self.departure_date.isoformat() if self.departure_date else None
        }
