from flask import Blueprint, jsonify, abort, make_response,request
from app.models.video import Video

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