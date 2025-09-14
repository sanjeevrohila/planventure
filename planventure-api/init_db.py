from app import app, db
from models import User, Trip
from datetime import datetime, timezone

def create_sample_data():
    """Create sample user and trip data"""
    # Create test user if it doesn't exist
    test_user = User.query.filter_by(email="test@example.com").first()
    if not test_user:
        test_user = User(email="test@example.com")
        test_user.set_password("password123")
        db.session.add(test_user)
        db.session.commit()
        print("Test user created successfully!")

    # Create test trip if it doesn't exist
    test_trip = Trip.query.filter_by(destination="Paris, France").first()
    if not test_trip:
        test_trip = Trip(
            user_id=test_user.id,
            destination="Paris, France",
            start_date=datetime(2025, 10, 1, tzinfo=timezone.utc),
            end_date=datetime(2025, 10, 7, tzinfo=timezone.utc),
            latitude=48.8566,
            longitude=2.3522,
            itinerary={
                "day1": ["Visit Eiffel Tower", "Seine River Cruise"],
                "day2": ["Louvre Museum", "Notre-Dame Cathedral"]
            }
        )
        db.session.add(test_trip)
        db.session.commit()
        print("Test trip created successfully!")

def init_db():
    """Initialize database and create sample data"""
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")
        
        # Create sample data
        create_sample_data()

if __name__ == "__main__":
    init_db()
