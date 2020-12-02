from flask import Flask

def create_app(config_object='flask_test.setting'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    mongo.init_app(app)
    return app
