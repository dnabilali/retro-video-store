from flask import Blueprint, jsonify, abort, make_response,request
from app.models.video import Video
from app import db

videos_bp = Blueprint("videos_bp",__name__, url_prefix="/videos")

@videos_bp.route("",methods=["GET"])
def get_all_videos():
    videos_query = Video.query

    videos = videos_query.all()
    videos_response = [video.to_dict() for video in videos]

    return jsonify(videos_response)

def validate_video_id(video_id):
    try:
        id = int(video_id)
    except:
        msg = f"Video id: {video_id} is Invalid"
        abort(make_response(jsonify({"details": msg}),400))

    video = Video.query.get(id)

    if video:
        return video

    msg = f"Video {video_id} was not found"
    abort(make_response(jsonify({"message": msg}),404))

@videos_bp.route("/<video_id>",methods=["GET"])
def get_video(video_id):
    video = validate_video_id(video_id)
    return jsonify(video.to_dict())  

@videos_bp.route("",methods=["POST"])
def create_video():
    request_body = request.get_json(silent=True)
    if not request_body:
        msg = "An empty or invalid json object was sent. Can't create video"
        abort(make_response(jsonify({"message":msg}),400))

    try:
        new_video = Video(
            title = request_body["title"],
            total_inventory = request_body["total_inventory"],
            release_date = request_body["release_date"]
        )

    except:
        msg = "Invalid json object sent from the request. Can't create video"
        abort(make_response(jsonify({"message":msg}),400))

    try:
        db.session.add(new_video)
        db.session.commit()

    except:
        msg = "Error creating video in db"
        abort(make_response(jsonify({"message":msg}),500))

    return make_response(jsonify(new_video.to_dict()),201)
