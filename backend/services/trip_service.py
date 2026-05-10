from models.trip_model import Trip
from models.destination_model import Destination
from models.expense_model import Expense
from extensions import db
from datetime import datetime

class TripService:
    @staticmethod
    def create_full_trip(user_id, data):
        try:
            # Create Trip
            trip = Trip(
                user_id=user_id,
                name=data.get('name'),
                description=data.get('description', ''),
                start_date=datetime.strptime(data.get('start_date'), '%Y-%m-%d').date() if data.get('start_date') else None,
                end_date=datetime.strptime(data.get('end_date'), '%Y-%m-%d').date() if data.get('end_date') else None,
                trip_type=data.get('trip_type', 'Solo'),
                status='upcoming'
            )
            db.session.add(trip)
            db.session.flush() # Get trip ID

            # Add Destinations
            for dest_data in data.get('destinations', []):
                dest = Destination(
                    trip_id=trip.id,
                    city=dest_data.get('city'),
                    country=dest_data.get('country'),
                    arrival_date=datetime.strptime(dest_data.get('arrival_date'), '%Y-%m-%d').date() if dest_data.get('arrival_date') else None,
                    departure_date=datetime.strptime(dest_data.get('departure_date'), '%Y-%m-%d').date() if dest_data.get('departure_date') else None
                )
                db.session.add(dest)

            # Add Expenses (initial budget estimates)
            budget = data.get('budget', {})
            for cat, amount in budget.items():
                if amount > 0:
                    exp = Expense(
                        trip_id=trip.id,
                        category=cat.capitalize(),
                        amount=amount,
                        description=f'Initial budget for {cat}',
                        date=trip.start_date or datetime.utcnow().date()
                    )
                    db.session.add(exp)

            db.session.commit()
            return trip, "Trip created successfully"
        except Exception as e:
            db.session.rollback()
            return None, str(e)
