from application import app
from application.continuous_resource_blueprint import blueprint as continuous_resource_blueprint
from flask import Flask, jsonify

def create_application() -> Flask:
    app.register_blueprint(continuous_resource_blueprint)
    return app

if __name__ == '__main__':
    app.run(port=5000, debug=True)
