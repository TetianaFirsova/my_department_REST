from flask import Flask
from config import app_config #Config
import os


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.secret_key = "Secret Key"

    from views.department import department
    app.register_blueprint(department)

    from views.employee import employee
    app.register_blueprint(employee)

    from views.home import home
    app.register_blueprint(home)

    return app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()