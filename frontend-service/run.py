from application import app
from application.continuous_resource_blueprint import blueprint as continuous_resource_blueprint
from flask import Flask, jsonify

# Register continuous resource blueprints
def create_application() -> Flask:
    app.register_blueprint(
            create_continuous_resource_blueprint(
                blueprint_name="FrontendService", # The name used by flask when using the url_for function
                resource_type="Frontend", # The resource type
                resource_prefix="frontend" # The base url for this resource type
                ),
            url_prefix='/api'

            )
    return app

if __name__ == '__main__':
    app.run(port=5000, debug=True)
