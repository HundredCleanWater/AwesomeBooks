from flask import Flask
from src.views.index_pages_bp import index_pages_bp
from src.apiRouter.apitest import search_page

app = Flask(__name__, instance_relative_config=True)


def register_blueprints_on_app(app):
    app.register_blueprint(index_pages_bp)
    app.register_blueprint(search_page)


register_blueprints_on_app(app)
