from flask import Request

from tests.integration import BaseTestCase
from tests.mocks.mock_test_task_neuro_responses import ResponseTestTaskNeuroResponses


def get(self, url: str, params=None) -> Request:
    return self.client.open(
        self.base_url(url),
        method="GET",
        query_string=params if params else {},
    )


class TestDistanceApi(BaseTestCase):
    """
    Integration test to Distance API
    """
    url = "distance"

    def test_integration_api_outside_mkad_passing_address_as_text(self):
        response = get(self, url=self.url, params={"address": "São Petesburg"})

        final_response = response.json

        self.assert200(response)
        self.assertEqual(ResponseTestTaskNeuroResponses.SAO_PETESBURG_OUTSIDE_MKAD_FINAL_RESPONSE, final_response)

    def test_integration_api_inside_mkad_passing_address_as_text(self):
        response = get(self, url=self.url, params={"address": "Bersenevskaya Naberezhnaya"})

        final_response = response.json

        self.assert200(response)
        self.assertEqual(ResponseTestTaskNeuroResponses.DESTINATION_INSIDE_MKAD_FINAL_RESPONSE, final_response)

    def test_integration_api_outside_mkad_passing_address_as_coordenate(self):
        response = get(self, url=self.url, params={"address": "48.8606111, 2.337644"})

        final_response = response.json

        self.assert200(response)
        self.assertEqual(ResponseTestTaskNeuroResponses.LOUVRE_OUTSIDE_MKAD_FINAL_RESPONSE, final_response)

    def test_integration_api_inside_mkad_passing_address_as_coordenate(self):
        response = get(self, url=self.url, params={"address": "55.745405, 37.612182"})

        final_response = response.json

        self.assert200(response)
        self.assertEqual(ResponseTestTaskNeuroResponses.DESTINATION_INSIDE_MKAD_FINAL_RESPONSE, final_response)


class TestDistanceApiBadScenarios(BaseTestCase):
    url = "distance"

    def test_bad_scenario_400(self):
        """
        Testing scenario of 400, doesent have the required query param "address"
        """
        response = get(self, url=self.url)
        self.assert_400(response)

    def test_bad_scenario_401(self):
        """
        Testing scenario of 401, doesent have google api key
        """
        response = get(self, url=self.url, params={"address": "São Petesburg"})
        self.assert_401(response)
