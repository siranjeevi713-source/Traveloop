from extensions import db

class Activity(db.Model):
    __tablename__ = 'activities'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.Enum('adventure', 'sightseeing', 'food', 'nightlife', 'trekking', 'cultural'), nullable=False)
    location = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    rating = db.Column(db.Numeric(2, 1))
    estimated_cost = db.Column(db.Numeric(10, 2))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'location': self.location,
            'image_url': self.image_url,
            'rating': float(self.rating) if self.rating else 0.0,
            'estimated_cost': float(self.estimated_cost) if self.estimated_cost else 0.0
        }
