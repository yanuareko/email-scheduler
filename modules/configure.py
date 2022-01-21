from flask_cors import CORS
from modules.config import load_config
from modules.extensions import mail, db, migrate


def configure_app(app):
    """To initialize flask app"""

    # get application config & db config value from config.yml
    app_config: dict = load_config("./config.yml")["application"]
    db_config: dict = load_config("./config.yml")["database"]
    celery_config: dict = load_config("./config.yml")["celery"]
    mail_config: dict = load_config("./config.yml")["mail"]

    # init Flask
    app.url_map.strict_slashes = False
    CORS(app, resources={r"/*": {"origins": "*"}})

    # put config value to Flask app
    app.config["TESTING"]: bool = app_config["testing"]
    app.config["ENV"]: str = app_config["env"]
    app.config["SECRET_KEY"]: str = "iSdu38sadf"
    app.config['port']: int = app_config["port"]
    app.config['base_api_url']: int = app_config["base_api_url"]
    app.config['log_folder']: int = app_config["log_folder"]
    # DB config
    app.config["SQLALCHEMY_DATABASE_URI"]: str = db_config["uri"]
    app.config['SQLALCHEMY_POOL_SIZE']: int = 100
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']: bool = False
    app.config['CORS_HEADERS']: str = 'Content-Type'
    # Celery config
    app.config['broker_url']: str = celery_config['broker_url']
    app.config['result_backend']: str = celery_config['result_backend']
    app.config['timezone']: str = celery_config['timezone']
    # Mail server config
    app.config['MAIL_SERVER'] = mail_config['server']
    app.config['MAIL_PORT'] = mail_config['port']
    app.config['MAIL_USE_TLS'] = mail_config['use_tls']
    app.config['MAIL_USERNAME'] = mail_config['username']
    app.config['MAIL_PASSWORD'] = mail_config['password']
    app.config['MAIL_DEFAULT_SENDER'] = mail_config['default_sender']


def configure_celery_app(app, celery):
    """Configures the celery app."""
    celery.conf.update(app.config)

    task_base = celery.Task

    class ContextTask(task_base):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return task_base.__call__(self, *args, **kwargs)

    celery.Task = ContextTask


def configure_extension(app):
    """Configure the extensions."""
    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Mail
    mail.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

