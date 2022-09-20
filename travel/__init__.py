from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    app.secret_key = "Super Secret Key"
    bootstrap = Bootstrap(app)

    # add Blueprints
    from . import views

    app.register_blueprint(views.mainbp)

    from . import destinations

    app.register_blueprint(destinations.bp)

    return app
