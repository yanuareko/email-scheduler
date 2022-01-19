import logging
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from resources.save_emails import PostSaveEmails


def handle_request(api: Api, app_config: dict, logger: logging.getLogger, db: SQLAlchemy):
    base_api_url = app_config["base_api_url"]
    api.add_resource(PostSaveEmails, base_api_url + '/save_emails',
                     resource_class_kwargs={'logger': logger, 'db': db})
