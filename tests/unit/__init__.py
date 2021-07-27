from unittest import TestCase

from tests.mocks.mock_google_requests import mock_google_request


class DefaultTestBase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        mock_google_request()
        print(f"\nRunning Class {self.__class__.__name__} -> Scenario: ", self.id().rpartition('.')[-1])

    def tearDown(self) -> None:
        print("Finished!\n")
        super().tearDown()
