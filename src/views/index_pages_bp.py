from flask import Blueprint, render_template, Response, session

index_pages_bp = Blueprint('index_pages_bp', __name__)

@index_pages_bp.route("/")
def index():
    user_id = session.get('user_id', None)
    return render_template("index.html")