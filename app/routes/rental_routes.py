from flask import Blueprint, request, make_response, jsonify, abort
from app.routes.customer_routes import validate_model
from app.models.customer import Customer
from app.models.video import Video
from app.models.rental import Rental
from app import db


rentals_bp = Blueprint("rentals_bp", __name__, url_prefix="/rentals")


@rentals_bp.route("/check-out", methods=["POST"])
def checkout_video_to_customer():
    request_body = request.get_json()
    required_data = ["customer_id", "video_id"]

    for data in required_data:
        if data not in request_body:
            abort(make_response(jsonify(
                    {"message": f"{data} required to complete this request."}), 400))

    valid_customer = validate_model(Customer, request_body["customer_id"])
    valid_video = validate_model(Video, request_body["video_id"])

    if valid_video.total_inventory < 1:
        abort(make_response(jsonify({"message":"Could not perform checkout"}), 400))

    new_rental = Rental(customer_id=valid_customer.id, video_id=valid_video.id)
    valid_video.total_inventory -= 1
    valid_customer.videos_checked_out_count += 1
    db.session.add(new_rental)
    db.session.commit()

    response_body = {
        "customer_id" : valid_customer.id,
        "video_id" : valid_video.id,
        "due_date" : new_rental.due_date,
        "videos_checked_out_count" : valid_customer.videos_checked_out_count,
        "available_inventory" : valid_video.total_inventory
    }

    return make_response(jsonify(response_body), 200)
