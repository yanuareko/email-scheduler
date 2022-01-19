from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from waitress import serve
from modules.config import load_config
from modules.create_app import create_app
from modules.create_logger import create_logger
from modules.request import handle_request


# get application config & db config value from config.yml
app_cfg: dict = load_config("./config.yml")["application"]
db_cfg: dict = load_config("./config.yml")["database"]

# logging
logger = create_logger(app_cfg["log_folder"])

# init Flask
app = create_app(app_cfg, db_cfg)

# use Api from flask_restful
api = Api(app)
db = SQLAlchemy(app)
handle_request(api, app_cfg, logger, db)

if __name__ == "__main__":
    environment = app_cfg["env"]
    print(f"""Running Backend with {environment} environment, port: {app_cfg["port"]}\n""")
    if environment == "production":
        serve(app, host="0.0.0.0", port=app_cfg["port"], threads=8)
    else:
        app.run(host="0.0.0.0", debug=app_cfg["testing"], port=app_cfg["port"], threaded=True)
