from typing import List

from models.coordinates import Coordinates
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
                               coordinates[0] is the initial address
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
        if self._status_ok_google(geocode_locations['status']):
            locations = [localization['geometry']['location'] for localization in geocode_locations['results']]

            return Coordinates(lat=locations[0]['lat'], lng=locations[0]['lng'])

        return Coordinates(None, None)

    def _format_google_response_distance_two_address(self, distance_between_address: dict) -> dict:
        """
        Format google api answer in a dict with the distance text and distance in meter.

        Example: { distance: "5 km", dinstance_in_meters: 3000 }
        """

        if self._status_ok_google(distance_between_address['status']):
            distances = [distance for distance in distance_between_address['rows'][0]['elements']]

            return {
                "distance": distances[0]['distance']['text'],
                "distance_in_meters": distances[0]['distance']['value']
            }

    @staticmethod
    def _status_ok_google(status: str) -> bool:
        """
        Checks if the status of google request was OK
        """

        if status == 'OK':
            return True

        return False
