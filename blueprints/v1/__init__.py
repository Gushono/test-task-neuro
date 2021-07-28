from flask import Blueprint
from flask_restplus import Api

from blueprints.v1.distance_model import namespace_distance as distance_api

blueprint = Blueprint('api', __name__, url_prefix='/v1')

api_extension = Api(
    blueprint,
    title='API RESTPLUS',
    version='1.0',
    description='Api REST',
    doc='/doc'
)

api_extension.add_namespace(distance_api)
