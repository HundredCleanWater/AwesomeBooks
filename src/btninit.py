from flask import Flask
from src.views.test_bp import test_bp


def register_blueprints_on_app(app):
    app.register_blueprint(test_bp)

app = Flask(__name__, instance_relative_config=True)

register_blueprints_on_app(app)