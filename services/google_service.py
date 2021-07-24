import json
import os

import requests

from configurations.logger import get_logger


class GoogleService:
    BASE_URL = 'https://maps.googleapis.com'
    API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")

    logger = get_logger()

    def get_to_google(self, path, parameters=None):
        """
        Make a GET to google

        :param path: Full URL to the api request
        :param parameters: Some params to make the api call. param key required

        :return: JSON with the response
        """

        if parameters is None:
            parameters = {}

        parameters.update({"key": self.API_KEY_GOOGLE})

        self.logger.info(f'Requesting to GOOGLE {path}...')

        r = requests.get(
            self.BASE_URL + path,
            params=parameters
        )
        if r.status_code == 200:
            self.logger.info("Successful Request")
            return json.loads(r.content)
        elif r.status_code == 400:
            self.logger.info("Bad Request")
            raise Exception
        elif r.status_code == 401:
            self.logger.error("Unauthorized Request")
            raise Exception
        elif r.status_code == 500:
            self.logger.error("Google internal server error")
            raise Exception
        else:
            self.logger.error("Untracked Error")
            raise Exception
