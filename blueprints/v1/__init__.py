from flask_restplus import Api
from flask import Blueprint
from blueprints.v1.distance_model import namespace as distance

blueprint = Blueprint('api', __name__, url_prefix='/v1')

api_extension = Api(
    blueprint,
    title='API RESTPLUS',
    version='1.0',
    description='Api REST',
    doc='/doc'
)

api_extension.add_namespace(distance)
