from flask import Blueprint, jsonify, abort, make_response,request
from app.models.video import Video

videos_bp = Blueprint("videos_bp",__name__, url_prefix="/videos")

@videos_bp.route("",methods=["GET"])
def get_all_videos():
    videos_query = Video.query

    videos = videos_query.all()
    videos_response = [video.to_dict() for video in videos]

    return jsonify(videos_response)
    