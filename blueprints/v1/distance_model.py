from typing import List

from flask_restplus import Namespace, Resource, fields, reqparse
from werkzeug.exceptions import BadRequest, Unauthorized

from configurations.logger import get_logger
from models.coordinates import Coordinates
from models.enums import EnumSituationsAnswers
from models.situation import Situation
from services.localization_service import LocalizationService

namespace = Namespace('distance', 'Distance of two address')

distance_model = namespace.model('Distance', {
    'distance_in_meters': fields.String(
        readonly=True,
        description='Return de distance in meters between two points'
    ),
    'distance_in_km': fields.String(
        readonly=True,
        description='Return de distance in km between two points'
    ),
    "situation": fields.Nested(
        namespace.model('Situation', {
            'id': fields.String(
                readonly=True,
                description='Return a enum of EnumSituationsAnswers',
                enum=[enum.name for enum in EnumSituationsAnswers]
            ),
            "description": fields.String(
                readonly=True,
                description='Return the description of the situation of the address',
            ),
        }))
})

parser = reqparse.RequestParser()
parser.add_argument('address', required=True, type=str)


@namespace.route('')
class Distance(Resource):

    @namespace.marshal_with(distance_model)
    @namespace.response(400, 'Bad Request')
    @namespace.response(401, 'Unauthorized! Google api key invalid or inexistent')
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(parser)
    def get(self):
        """
        This endpoint will return the distance between MKAD and a target address. And if it is inside or outside MKAD
        """

        logger = get_logger()
        localization_service = LocalizationService()

        try:

            address_name = parser.parse_args()

            if self._has_address_as_parameter(address_name):

                final_address_cordinate = localization_service.get_to_google_lat_and_lng(address_name['address'])

                coordinates = [final_address_cordinate]

                if self._check_coordinates_is_valid(coordinates):

                    if localization_service.verify_if_address_is_inside_mkad(coordinates[0]):
                        return Situation(id=EnumSituationsAnswers.INSIDE_MKAD.name,
                                         description=EnumSituationsAnswers.INSIDE_MKAD.value).to_json()

                    return localization_service.get_distance_between_mkad_and_destination_address(coordinates)

        except BadRequest as ex:
            logger.error(f"BAD REQUEST! {ex.description}")
            raise ex
        except Unauthorized as ex:
            logger.error(f"UNAUTHORIZED! {ex.description}")
            raise ex

    @staticmethod
    def _has_address_as_parameter(address: dict) -> bool:
        """
        Verify the existence of a query parameter called address

        :params: address -> Dict with query params info inside
        """

        return True if address['address'] is not None else False

    @staticmethod
    def _check_coordinates_is_valid(coordinates: List[Coordinates]) -> bool:
        """
        Validates if all objects of Coordinate has values inside lat and lng attributes.

        :params: coordinates -> List of coordinates found from GOOGLES APIs
        """
        coordinates_lat_lng_valid = [True if coordinate.lat and coordinate.lng else False for coordinate in coordinates]

        if all(coordinates_lat_lng_valid):
            return True

        raise BadRequest("BAD REQUEST! Address not found at google's api")
