from typing import List

from flask_restplus import Namespace, Resource, fields, reqparse
from werkzeug.exceptions import BadRequest

from configurations.logger import get_logger
from models.coordinates import Coordinates
from services.localization_service import LocalizationService

namespace = Namespace('distance', 'Distance of two address')

distance_model = namespace.model('Distance', {
    'distance_in_meters': fields.String(
        readonly=True,
        description='Return de distance in meters between two points'
    ),
    'distance': fields.String(
        readonly=True,
        description='Return de distance in km between two points'
    )
})

parser = reqparse.RequestParser()
parser.add_argument('address', type=str)


@namespace.route('')
class Distance(Resource):

    @namespace.marshal_with(distance_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(404, 'Not Found')
    @namespace.expect(parser)
    def get(self):
        """
        This endpoint will return the distance between two points

        :return: An object of Distance
        """

        logger = get_logger()
        localization_service = LocalizationService()
        address_name = parser.parse_args()

        logger.info("Requesting to GOOGLE APIS to search lat and lng...")
        initial_address_cordinate = localization_service.get_to_google_lat_and_lng("MKAD")
        final_address_cordinate = localization_service.get_to_google_lat_and_lng(address_name['address'])

        coordinates = [initial_address_cordinate, final_address_cordinate]

        if self.check_cordinates_is_valid(coordinates):
            logger.info("Requesting to GOOGLE APIS to search the distance between the two address...")
            distance_between_address = localization_service.get_distance_between_two_cordinates(coordinates)
            return distance_between_address

        raise BadRequest("Address not found at google's api")

    @staticmethod
    def check_cordinates_is_valid(coordinates: List[Coordinates]) -> bool:
        coordinates_lat_lng_valid = [True if coordinate.lat and coordinate.lng else False for coordinate in coordinates]

        if all(coordinates_lat_lng_valid):
            return True

        return False
