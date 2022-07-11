from application import app
from application.continuous_resource_blueprint import blueprint as continuous_resource_blueprint
from flask import Flask, jsonify

def create_application() -> Flask:
    app.register_blueprint(
            create_continuous_resource_blueprint(
                blueprint_name="NewsService", # The name used by flask when calling the url_for function
                resource_type="News",
                resource_prefix="news"

                ),
            url_prefix='/api'

            )
    return app


if __name__ == '__main__':
    app.run(port=5002, debug=True)
