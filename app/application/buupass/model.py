from .. import db


class PaymentMode(db.Model):
    __tablename__ = "paymentmodes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    payment_type = db.Column(db.String(64), index=True, unique=True, nullable=False)
    cardNumber = db.Column(db.String(64), index=True, unique=True, nullable=False)
    cvv = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=False)


class Travellers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phone_number = db.Column(db.String(64))
    origin = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=False)
    # historys = db.relationship('BookingHistory', backref='history', lazy='dynamic')


class BookingHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    date = db.Column(db.String(64))
    price = db.Column(db.String(64))


class BookMarks(db.Model):
    """
    The things a user has bookmarked for future reference...
    query them in ascending order by date.
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(64))
    price = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, nullable=False)


class Subscriptions(db.Model):
    """
    These are the notifications the user has subscribed to / they want to
    receive these notifications.
    This should be linked to a user...
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(64))


class Preferences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64))
    home_airport = db.Column(db.String(64))
    email_site = db.Column(db.String(64))
    password = db.Column(db.String(64))
    default_language = db.Column(db.String(64))
    default_currency = db.Column(db.String(64))
    temperature = db.Column(db.String(64))
    modified_at = db.Column(db.DateTime, nullable=False)


hotels = [
    {
        "location": "Newyork",
        "start_date": "SAT 6/27",
        "end_date": "SUN 6/28",
        "no_of_rooms": "1",
        "capacity": "1",
        "name": "HOLIDAY INN",
    },
    {
        "location": "Newyork",
        "start_date": "SAT 6/27",
        "end_date": "SUN 6/28",
        "no_of_rooms": "1",
        "capacity": "1",
        "name": "INTERCONTINENTAL",
    },
    {
        "location": "Newyork",
        "start_date": "SAT 6/27",
        "end_date": "SUN 6/28",
        "no_of_rooms": "1",
        "capacity": "1",
        "name": "SERENA",
    },
    {
        "location": "Newyork",
        "start_date": "SAT 6/27",
        "end_date": "SUN 6/28",
        "no_of_rooms": "1",
        "capacity": "1",
        "name": "WHITE SANDS",
    },
    {
        "location": "Newyork",
        "start_date": "SAT 6/27",
        "end_date": "SUN 6/28",
        "no_of_rooms": "1",
        "capacity": "1",
        "name": "RADISON BLU",
    },
]

flights = [
    {
        "departure": "1100hrs",
        "arrival": "1800hrs",
        "destination": "Nairobi",
        "route": "Amsterdam",
        "airline": "KLM",
        "capacity": 260,
    },
    {
        "departure": "1200hrs",
        "arrival": "1900hrs",
        "destination": "Newyork",
        "route": "direct",
        "airline": "Kenya Airways",
        "capacity": 140,
    },
    {
        "departure": "1200hrs",
        "arrival": "1900hrs",
        "destination": "Newyork",
        "route": "Heathrow",
        "airline": "Rwanda Air",
        "capacity": 140,
    },
    {
        "departure": "1200hrs",
        "arrival": "1900hrs",
        "destination": "Newyork",
        "route": "Dubai",
        "airline": "Qatar",
        "capacity": 190,
    },
    {
        "departure": "1200hrs",
        "arrival": "1900hrs",
        "destination": "Newyork",
        "route": "instabul",
        "airline": "Turkey ",
        "capacity": 170,
    },
]

experiences = [
    {"experience": "swimming"},
    {"experience": "boxing"},
    {"experience": "surfing"},
]

cars = [
    {"capacity": 4, "type": "Mazda", "price": 5000},
    {"capacity": 3, "type": "Tuktuk", "price": 2000},
    {"capacity": 8, "type": "Noah", "price": 10000},
    {"capacity": 8, "type": "V8", "price": 20000},
    {"capacity": 5, "type": "SUV", "price": 9000},
]

homes = [
    {"location": "Newyork", "no_of_rooms": "1", "capacity": "1"},
    {"location": "Mumbai", "no_of_rooms": "1", "capacity": "1"},
    {"location": "Tokyo", "no_of_rooms": "1", "capacity": "1"},
    {"location": "Wuhan", "no_of_rooms": "1", "capacity": "1"},
    {"location": "Nairobi", "no_of_rooms": "1", "capacity": "1"},
]
