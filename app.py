from flask import Flask
from waitress import serve
from modules.configure import configure_app, configure_celery_app, configure_extension
from modules.api_request import handle_request
from modules.extensions import celery


def create_app() -> Flask:
    """To initialize flask app"""
    # init Flask
    flask_app: Flask = Flask("email-scheduler", template_folder='templates')
    flask_app.url_map.strict_slashes = False

    configure_app(flask_app)
    configure_celery_app(flask_app, celery)
    configure_extension(flask_app)

    return flask_app


app = create_app()
celery.conf.update(app.config)

handle_request(app)

if __name__ == "__main__":
    environment = app.config["ENV"]
    print(f"""Running Backend with {environment} environment, port: {app.config["port"]}\n""")
    if environment == "production":
        serve(app, host="0.0.0.0", port=app.config["port"], threads=8)
    else:
        app.run(host="0.0.0.0", debug=app.config["TESTING"], port=app.config["port"], threaded=True)
