from flask import Blueprint, jsonify, abort, make_response,request
from app.models.video import Video
from app.models.rental import Rental
from app import db
from app.routes.helpers import validate_model, validate_request_body

videos_bp = Blueprint("videos_bp",__name__, url_prefix="/videos")

required_data = ["title","total_inventory","release_date"]

@videos_bp.route("",methods=["GET"])
def get_all_videos():
    videos_query = Video.query

    videos = videos_query.all()
    videos_response = [video.to_dict() for video in videos]

    return jsonify(videos_response)

@videos_bp.route("/<video_id>",methods=["GET"])
def get_video(video_id):
    video = validate_model(Video,video_id)
    return jsonify(video.to_dict())  

@videos_bp.route("",methods=["POST"])
def create_video():
    request_body = request.get_json(silent=True)
    validate_request_body(request_body,required_data)

    new_video = Video(
            title = request_body["title"],
            total_inventory = request_body["total_inventory"],
            # available_inventory = request_body["total_inventory"],
            release_date = request_body["release_date"]
    )

    try:
        db.session.add(new_video)
        db.session.commit()

    except:
        msg = "Error creating video in db"
        abort(make_response(jsonify({"message":msg}),500))

    return make_response(jsonify(new_video.to_dict()),201)

@videos_bp.route("/<video_id>",methods=["PUT"])    
def update_video(video_id):
    video = validate_model(Video,video_id)

    request_body = request.get_json(silent=True)
    validate_request_body(request_body,required_data)

    video.title = request_body["title"]
    video.total_inventory = request_body["total_inventory"]
    video.release_date = request_body["release_date"]

    db.session.commit()

    return make_response(jsonify(video.to_dict()),200)

@videos_bp.route("/<video_id>",methods=["DELETE"]) 
def delete_video(video_id):
    video = validate_model(Video,video_id)

    db.session.delete(video)
    db.session.commit()

    return make_response(jsonify({"id":video.id}),200)

@videos_bp.route("<video_id>/rentals", methods=["GET"])
def list_customers_renting_video(video_id):
    valid_video = validate_model(Video,video_id)
    all_customers_with_video = valid_video.customers
    response = []

    for customer in all_customers_with_video:
        rental = Rental.query.filter_by(customer_id=customer.id, video_id=video_id).first()
        response.append({
            "due_date": rental.due_date,
            "name": customer.name,
            "phone": customer.phone,
            "postal_code": customer.postal_code,
        })

    return make_response(jsonify(response), 200)