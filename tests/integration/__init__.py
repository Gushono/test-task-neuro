from flask_testing import TestCase

from main import init_api


class BaseTestCase(TestCase):

    def create_app(self):
        print(f"\nRunning Class {self.__class__.__name__} -> Scenario: ", self.id().rpartition('.')[-1])

        app = init_api()
        return app

    @staticmethod
    def base_url(url):
        return f"/v1/{url}"
