from services.geocode import GeocodeApi

from test.unit import DefaultTestBase


class TestDistanceApi(DefaultTestBase):

    def test_received_yandex_geo_code(self):
        geo_code = GeocodeApi()

        response = geo_code.get_to_yandex_geo_code('a')
        self.assertEqual({'a': 'a'}, response)

    def test_calculate_distance(self):
        distance = 3 + 3

        self.assertEqual(6, distance)
