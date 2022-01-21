from flask import Flask
from resources.home import GetHome
from flask_restful import Api
from resources.save_emails import PostSaveEmails
from resources.events import PostCreateEvent, GetManageEvent


def handle_request(app: Flask):
    api = Api(app)
    base_api_url = app.config["base_api_url"]

    @app.before_request
    def before_request():
        # When you import jinja2 macros, they get cached which is annoying for local
        # development, so wipe the cache every request.
        app.jinja_env.cache = {}

    api.add_resource(GetHome, base_api_url + '/')
    api.add_resource(PostCreateEvent, base_api_url + '/create_event')
    api.add_resource(PostSaveEmails, base_api_url + '/save_emails', resource_class_kwargs={'app': app})
    api.add_resource(GetManageEvent, base_api_url + '/manage/<int:event_id>')

