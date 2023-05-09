from flask import Flask
from app.conn_db import config_database
from app.routes import config_routes


def app_start():

    app = Flask(__name__)

    config_routes(app)
    config_database(app)

    return app


APP = app_start()

if __name__ == '__main__':
    APP.run(debug=True)
