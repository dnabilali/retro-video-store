from app import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    postal_code = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    register_at = db.Column(db.DateTime, nullable=False)
    videos_checked_out_count = db.Column(db.Integer, nullable=False)

