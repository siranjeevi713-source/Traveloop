from extensions import db

class PackingList(db.Model):
    __tablename__ = 'packing_lists'
    
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    item_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.Enum('Clothes', 'Electronics', 'Documents', 'Medicines', 'Essentials', 'Other'), default='Other')
    is_packed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'item_name': self.item_name,
            'category': self.category,
            'is_packed': self.is_packed
        }
