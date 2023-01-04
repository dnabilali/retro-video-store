from app import db
import datetime

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    postal_code = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    registerd_at = db.Column(db.String, default=datetime.datetime.now().strftime("%a, %d %b %Y %X %z"))
    videos_checked_out_count = db.Column(db.Integer, nullable=False, default=0)
