# This is a  stattic Blueprint which has the resource type as a dynamic element in the url
# Each route function will need to validate the resource type

from flask import Blueprint, jsonify

blueprint = Blueprint('ContinuousResourceBlueprint', __name__)

@blueprint.route('/<resource_type>', methods=['POST'])
def create_continuous_resource(resource_type):
    return jsonify({}), 201

