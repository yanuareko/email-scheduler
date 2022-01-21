from flask import Flask
from resources.home import GetHome
from flask_restful import Api
from resources.save_emails import PostSaveEmails
from resources.create_event import CreateEvent


def handle_request(app: Flask):
    api = Api(app)
    base_api_url = app.config["base_api_url"]

    @app.before_request
    def before_request():
        # When you import jinja2 macros, they get cached which is annoying for local
        # development, so wipe the cache every request.
        app.jinja_env.cache = {}

    # @app.route('/', methods=['GET'])
    # def home_index():
    #     return render_template("index.html")

    # @app.route('/save_emails', methods=['GET', 'POST'])
    # def save_emails():
    #     return render_template("save_emails.html")

    # endpoint for / 'home'
    api.add_resource(GetHome, base_api_url + '/')

    # endpoint for /create_event
    api.add_resource(CreateEvent, base_api_url + '/create_event')

    # endpoint for /save_emails
    api.add_resource(PostSaveEmails, base_api_url + '/save_emails',
                     resource_class_kwargs={'app': app})
