from application import app
from application.continuous_resource_blueprint import blueprint as continuous_resource_blueprint
from flask import Flask, jsonify

def create_application() -> Flask:
    app.register_blueprint(
            create_continuous_resource_blueprint(
                blueprint_name="LoginService", # The name used by flask when calling url_for function
                resource_type="Login",
                resource_prefix="login" # Base url for this resource type

                ),
            url_prefix='/api'

            )

    return app

if __name__ == '__main__':
    app.run(port=5001, debug=True)

