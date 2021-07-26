from typing import List
from urllib.parse import ParseResult

from flask_restplus import Namespace, Resource, fields, reqparse
from werkzeug.exceptions import BadRequest

from configurations.logger import get_logger
from models.coordinates import Coordinates
from models.enums import EnumSituationsAnswers
from services.localization_service import LocalizationService

namespace = Namespace('distance', 'Distance of two address')

distance_model = namespace.model('Distance', {
    'distance_in_meters': fields.String(
        readonly=True,
        description='Return de distance in meters between two points'
    ),
    'distance': fields.String(
        readonly=True,
        description='Return de distance (text) between two points'
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
    @namespace.response(500, 'Internal Server error')
    @namespace.response(400, 'Bad Request')
    @namespace.expect(parser)
    def get(self):
        """
        This endpoint will return the distance between MKAD and a target address. And if it is inside or outside MKAD
        """

        logger = get_logger()
        localization_service = LocalizationService()

        try:

            address_name = parser.parse_args()

            if self.has_address(address_name):

                logger.info(f"Requesting to GOOGLE APIS to search lat and lng of {address_name['address']}...")
                initial_address_cordinate = localization_service.get_to_google_lat_and_lng("MKAD")
                final_address_cordinate = localization_service.get_to_google_lat_and_lng(address_name['address'])

                coordinates = [initial_address_cordinate, final_address_cordinate]

                if self.check_cordinates_is_valid(coordinates):
                    logger.info("Requesting to GOOGLE APIS to search the distance between the two address...")
                    distance_between_address = localization_service.get_distance_between_two_cordinates(coordinates)
                    return distance_between_address

                raise BadRequest("BAD REQUEST! Address not found at google's api")
        except BadRequest as ex:
            logger.error(f"BAD REQUEST! {ex.description}")
            raise ex

    @staticmethod
    def has_address(address: ParseResult) -> bool:
        """
        Verify the existence of a query parameter called address

        :params: address -> Object of type ParseResult with query params info inside
        """

        return True if address['address'] is not None else False

    @staticmethod
    def check_cordinates_is_valid(coordinates: List[Coordinates]) -> bool:
        """
        Validates if all objects of Coordinate has values inside lat and lng attributes.

        :params: coordinates -> List of coordinates found from GOOGLES APIs
        """
        coordinates_lat_lng_valid = [True if coordinate.lat and coordinate.lng else False for coordinate in coordinates]

        if all(coordinates_lat_lng_valid):
            return True

        return False
