from typing import List

from models.coordinates import Coordinates
from models.enums import EnumSituationsAnswers
from services.google_service import GoogleService


class LocalizationService:
    GEOCODE_GOOGLE_API = "/maps/api/geocode/json"
    MATRIX_GOOGLE_API = "/maps/api/distancematrix/json"

    _google_api = GoogleService()

    def get_to_google_lat_and_lng(self, address: str) -> Coordinates:
        """
        Api request responsable to return the lat and lng from an address

        :param: address -> Address that you want to know the LAT AND LNG
        """

        params = {
            "address": address,
        }

        response = self._google_api.get_to_google(self.GEOCODE_GOOGLE_API, parameters=params)

        return self._format_google_response_to_lat_long(response)

    def get_distance_between_two_cordinates(self, coordinates: List[Coordinates]) -> dict:
        """
        Function responsable to return the distance between two cordinates

        :param: coordinates -> List of Coordinates objects.
                               coordinates[0] is the initial address (MKAD)
                               coordinates[1] is the target address

        """

        params = {
            "origins": f"{coordinates[0].lat}, {coordinates[0].lng}",
            "destinations": f"{coordinates[1].lat}, {coordinates[1].lng}",
        }

        response = self._google_api.get_to_google(self.MATRIX_GOOGLE_API, parameters=params)

        return self._format_google_response_distance_two_address(response)

    def _format_google_response_to_lat_long(self, geocode_locations: dict) -> Coordinates:
        """
        Format google api answer in a dict with lat and long.

        Example: { lat: -22.9175898, long: -22.9175898 }
        """
        if self._status_suceffuly_google(geocode_locations['status']):
            locations = [localization['geometry']['location'] for localization in geocode_locations['results']]

            return Coordinates(lat=locations[0]['lat'], lng=locations[0]['lng'])

        return Coordinates(None, None)

    def _format_google_response_distance_two_address(self, distance_between_address: dict) -> dict:
        """
        Format google api answer in a dict with the distance text, distance in meter and the situation.

        Example: { distance: "5 km", distance_in_meters: 3000 }
        """

        if self._status_suceffuly_google(distance_between_address['rows'][0]['elements'][0]['status']):
            distances = [distance for distance in distance_between_address['rows'][0]['elements']]

            return {
                "distance": distances[0]['distance']['text'],
                "distance_in_meters": distances[0]['distance']['value'],
                "situation": {
                    "id": EnumSituationsAnswers.OUTSIDE_MKAD.name,
                    "description": EnumSituationsAnswers.OUTSIDE_MKAD.value
                }
            }

        return {
            "situation": {
                "id": EnumSituationsAnswers.GOOGLE_API_CANNOT_CALCULATE_DISTANCE.name,
                "description": EnumSituationsAnswers.GOOGLE_API_CANNOT_CALCULATE_DISTANCE.value
            }
        }

    @staticmethod
    def _status_suceffuly_google(status: str) -> bool:
        """
        Checks if the status of google request was OK and has
        """

        if status == 'OK' or status != 'ZERO_RESULTS':
            return True

        return False
