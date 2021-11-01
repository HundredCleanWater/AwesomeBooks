from flask import Flask
from src.views.index_pages_bp import index_pages_bp
from src.views.login_pages_bp import login_pages_bp
from src.views.signup_pages_bp import signup_pages_bp
from src.apiRouter.apitest import search_page


def register_blueprints_on_app(app):
    app.register_blueprint(index_pages_bp)
    app.register_blueprint(search_page)
    app.register_blueprint(signup_pages_bp)

app = Flask(__name__, instance_relative_config=True)
app.config["SECRET_KEY"] = "x5k45ggr"

register_blueprints_on_app(app)