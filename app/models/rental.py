from app import db
# from datetime import datetime, timedelta

class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey("video.id"), nullable=False)
    due_date = db.Column(db.DateTime)

    # def video_to_dict(self):
    #     return {
    #         "id": self.video.id,
    #         "title": self.video.title,
    #         "total_inventory": self.video.total_inventory,
    #         "release_date": self.video.release_date
    #     }