import json

from services.localization_service import LocalizationService
from tests.unit import DefaultTestBase
from tests.unit.mocks.mocks_googles_responses import ResponseJsonMocks


class TestLocalizationService(DefaultTestBase):
    localization = LocalizationService()

    def test_format_google_response_to_lat_long(self) -> None:
        """
        Test using the MOCKED MKAD location

        """

        response = self.localization._format_google_response_to_lat_long(json.loads(
            ResponseJsonMocks.RESPONSE_GOOGLE_MKAD_LOCATION)
        )

        self.assertEqual(55.6909315, response.lat)
        self.assertEqual(37.4130217, response.lng)

    def test_format_google_response_distance_two_address(self) -> None:
        """
        Test using the the mocked distance between MKAD and MOSCOW
        """

        response = self.localization._format_google_response_distance_two_address(json.loads(
            ResponseJsonMocks.RESPONSE_GOOGLE_DISTANCE_MKAD_TO_MOSCOW
        ))

        self.assertEqual({'distance': '19.4 km', 'distance_in_meters': 19411}, response)

    def test_status_ok_google(self) -> None:
        """
        Test if the google status is OK
        """
        response = self.localization._status_ok_google('OK')

        self.assertTrue(response)
