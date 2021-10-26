from flask import Blueprint, render_template

test_bp = Blueprint('test_bp', __name__)

@test_bp.route("/")
def index():
    name = "제발"
    return render_template("index.html", data=name)