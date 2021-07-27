import json

from services.localization_service import LocalizationService
from tests.unit import DefaultTestBase
from tests.unit.mocks.mock_test_task_neuro_responses import ResponseTestTaskNeuroResponses
from tests.unit.mocks.mocks_googles_responses import ResponseGoogleJsonMocks


class TestLocalizationService(DefaultTestBase):
    localization_service = LocalizationService()

    def test_format_google_response_to_lat_long(self) -> None:
        response = self.localization_service._format_google_response_to_lat_long(json.loads(
            ResponseGoogleJsonMocks.RESPONSE_GOOGLE_MKAD_LOCATION)
        )

        self.assertEqual(55.6909315, response.lat)
        self.assertEqual(37.4130217, response.lng)

    def test_check_google_request_status(self) -> None:
        response = self.localization_service._check_google_request_status('OK')
        self.assertTrue(response)

    def test_calculate_distance_between_mkad_and_other_coordinate(self) -> None:
        response_km, response_meters = self.localization_service._calculate_distance_between_mkad_and_other_coordinate(
            ResponseTestTaskNeuroResponses.SAO_PETESBURG_COORDINATE
        )

        self.assertEqual(632.422026686628, response_km)
        self.assertEqual(632422.026686628, response_meters)

    def test_format_response_distance_of_two_address(self) -> None:
        response = self.localization_service._format_response_distance_of_two_address(
            ResponseTestTaskNeuroResponses.DISTANCES_IN_KM_AND_METERS
        )

        # Testing if the float value has been converted in str
        self.assertTrue(isinstance(response['distance_in_km'], str))
        self.assertTrue(isinstance(response['distance_in_meters'], str))

        self.assertEqual("3.00", response['distance_in_km'])
        self.assertEqual("3000.00", response['distance_in_meters'])

        self.assertEqual("OUTSIDE_MKAD", response['situation']['id'])
        self.assertEqual("The destination address is outside of MKAD", response['situation']['description'])

    def test_check_if_radius_circle_is_bigger_than_destination_distance(self) -> None:
        response_true = self.localization_service._check_if_radius_circle_is_bigger_than_destination_distance(
            18.00
        )

        response_false = self.localization_service._check_if_radius_circle_is_bigger_than_destination_distance(
            20.00
        )

        self.assertTrue(response_true)
        self.assertFalse(response_false)

    def test__format_to_two_decimal_points(self) -> None:
        response = self.localization_service._format_to_two_decimal_points(3000.493338)

        self.assertTrue(isinstance(response, str))

        self.assertEqual("3000.49", response)
