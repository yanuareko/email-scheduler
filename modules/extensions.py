from celery import Celery
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# celery.Celery
celery = Celery("email-scheduler")

# Database
db = SQLAlchemy()

# Flask-Mail
mail = Mail()

# Flask-Migrate
migrate = Migrate()

