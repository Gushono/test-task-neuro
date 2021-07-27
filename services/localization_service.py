from typing import List, Tuple

from haversine import haversine
from werkzeug.exceptions import Unauthorized

from configurations.logger import get_logger
from models.coordinates import Coordinates
from models.enums import EnumSituationsAnswers
from models.situation import Situation
from services.google_service import GoogleService


class LocalizationService:
    GEOCODE_GOOGLE_API = "/maps/api/geocode/json"

    CENTER_OF_MKAD = (55.745405, 37.612182)
    POINT_OF_THE_CIRCLE = (55.572313, 37.665133)
    RADIUS_OF_THE_CIRCLE = 19.53146957984939  # This is the result of haversine of (CENTER_OF_MKAD, POINT_OF_THE_CIRCLE)

    _google_api = GoogleService()
    _logger = get_logger()

    def get_to_google_lat_and_lng(self, address: str) -> Coordinates:
        """
        Api request responsable to return the lat and lng from an address

        :param: address -> Address that you want to know the LAT AND LNG
        """

        params = {
            "address": address,
        }

        self._logger.info(f"Requesting to GOOGLE APIS to search lat and lng of {address}...")
        response = self._google_api.get_to_google(self.GEOCODE_GOOGLE_API, parameters=params)

        return self._format_google_response_to_lat_long(response)

    def get_distance_between_mkad_and_destination_address(self, coordinates: List[Coordinates]) -> dict:
        """
        Function responsable to return the distance between two coordinates in killometers and meters

        :param: coordinates -> List of Coordinates objects.
                               coordinates[0] is the destination address

        """

        self._logger.info("Calculating distance between mkad and target address...")

        distance_in_km, distance_in_meters = self._calculate_distance_between_mkad_and_other_coordinate(
            coordinates[0].to_tuple()
        )

        distances = {
            "distance_in_km": distance_in_km,
            "distance_in_meters": distance_in_meters
        }

        return self._format_response_distance_of_two_address(distances)

    def verify_if_address_is_inside_mkad(self, destination_coordenate: Coordinates) -> bool:
        """
        Verify if the address is inside of mkad using a circle as reference.

        Using haversine to calculate the distance between two coordenates and using radius

        """

        distance_in_km, distance_in_meters = self._calculate_distance_between_mkad_and_other_coordinate(
            destination_coordenate.to_tuple()
        )

        self._logger.info(f"Calculated radius of the circle is {self.RADIUS_OF_THE_CIRCLE}")
        self._logger.info(f"Calculated distance of the destination {distance_in_km}")

        if self._check_if_radius_circle_is_bigger_than_destination_distance(distance_in_km):
            self._logger.info(f"Destination address {destination_coordenate.to_tuple()} is inside MKAD!")
            return True

        return False

    def _format_google_response_to_lat_long(self, geocode_locations: dict) -> Coordinates:
        """
        Format google api answer in a dict with lat and long.

        Example: { lat: -22.9175898, long: -22.9175898 }
        """
        if self._check_google_request_status(geocode_locations['status']):
            locations = [localization['geometry']['location'] for localization in geocode_locations['results']]

            return Coordinates(lat=locations[0]['lat'], lng=locations[0]['lng'])

        return Coordinates(None, None)

    def _check_google_request_status(self, status: str) -> bool:
        """
        Check if google request has a succesful complete
        """

        if status == 'OK':
            return True
        elif status == 'ZERO_RESULTS':
            self._logger.info("Request to google didn't found any result with this search!")
            return False
        elif status == 'REQUEST_DENIED':
            raise Unauthorized("UNAUTHORIZED! Google's api key is invalid, inexistent or your IP is not allowed")

        return False

    def _calculate_distance_between_mkad_and_other_coordinate(self, any_coordinate: tuple) -> Tuple[float, float]:
        """
        Function that calculates the distance between two coordinates using haversine formula
        and returning in METERS AND KM
        """
        distance_of_two_coordenates_in_km = haversine(self.CENTER_OF_MKAD, any_coordinate, unit='km')
        distance_of_two_coordenates_in_meters = haversine(self.CENTER_OF_MKAD, any_coordinate, unit='m')

        return distance_of_two_coordenates_in_km, distance_of_two_coordenates_in_meters

    def _format_response_distance_of_two_address(self, distances: dict) -> dict:
        """
        Format answer in a dict with the distance in km, distance in meter and the situation.
        """

        return {
            "distance_in_km": self._format_to_two_decimal_points(distances['distance_in_km']),
            "distance_in_meters": self._format_to_two_decimal_points(distances['distance_in_meters']),
            "situation": Situation(id=EnumSituationsAnswers.OUTSIDE_MKAD.name,
                                   description=EnumSituationsAnswers.OUTSIDE_MKAD.value).__dict__
        }

    def _check_if_radius_circle_is_bigger_than_destination_distance(self, distance: float) -> bool:
        """
        If radius in km of the circle drawed around of MKAD is bigger than destination_distance

        It means that if RADIUS_OF_THE_CIRCLE is bigger -> Inside of MKAD
                                                 lower  -> Ouside of MKAD

        """
        if self.RADIUS_OF_THE_CIRCLE > distance:
            return True

        return False

    @staticmethod
    def _format_to_two_decimal_points(distance: float) -> str:
        """
        Format a float value in two decimal points
        """

        return format(distance, '.2f')
