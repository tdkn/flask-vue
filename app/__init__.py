from flask import Flask


def create_app():
    """
    Create a Flask app
    :rtype: Flask
    :return: Flask instance
    """
    app = Flask(__name__)

    configure_blueprints(app)
    configure_database(app)
    configure_assets(app)

    return app


def configure_blueprints(app):
    """
    Configure Blueprints
    :param Flask app:
    """
    from app.views import index, hello

    for view in [index, hello]:
        app.register_blueprint(view.blueprint)


def configure_database(app):
    """
    Configure Database
    :param Flask app:
    """
    from app.database import db

    db.init_app(app)


def configure_assets(app):
    """
    Configure Assets
    :param Flask app:
    """
    from app.webassets import webassets

    webassets.init_app(app)
    with app.app_context():
        webassets.load_path = ['assets']
