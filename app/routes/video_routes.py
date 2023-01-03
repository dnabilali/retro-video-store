from flask import Blueprint, jsonify, abort, make_response,request
from app.models.video import Video

videos_bp = Blueprint("videos_bp",__name__, url_prefix="/videos")

