from flask import Flask
from flask_cors import CORS


def create_app(app_config: dict, db_config: dict) -> Flask:
    """
    To initialize flask app
    :param app_config: application configuration from config.yml
    :param db_config: database configuration from config.yml
    :return: Flask object
    """
    environment: str = app_config["env"]
    is_test: bool = app_config["testing"]

    sql_db_uri: str = db_config["uri"]

    # init Flask
    app: Flask = Flask(__name__)
    app.url_map.strict_slashes = False
    CORS(app, resources={r"/*": {"origins": "*"}})

    # put config value to Flask app
    app.config["TESTING"]: bool = is_test
    app.config["ENV"]: str = environment
    app.config["SQLALCHEMY_DATABASE_URI"]: str = sql_db_uri
    app.config['SQLALCHEMY_POOL_SIZE']: int = 100
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']: bool = False
    app.config['CORS_HEADERS']: str = 'Content-Type'

    return app
