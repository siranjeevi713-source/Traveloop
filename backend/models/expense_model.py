from extensions import db

class Expense(db.Model):
    __tablename__ = 'expenses'
    
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    category = db.Column(db.Enum('hotel', 'transport', 'food', 'shopping', 'activities', 'emergency', 'other'), default='other')
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.String(255))
    expense_date = db.Column(db.Date)

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'category': self.category,
            'amount': float(self.amount),
            'description': self.description,
            'expense_date': self.expense_date.isoformat() if self.expense_date else None
        }
