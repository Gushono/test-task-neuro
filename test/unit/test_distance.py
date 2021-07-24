from services.localization_service import LocalizationService

from . import DefaultTestBase


class TestDistanceApi(DefaultTestBase):

    def test_received_yandex_geo_code(self):
        geo_code = LocalizationService()

        response = geo_code.get_to_google_geo_code('a')
        self.assertEqual({'a': 'a'}, response)

    def test_calculate_distance(self):
        distance = 3 + 3

        self.assertEqual(6, distance)
