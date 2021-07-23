import json

import requests as r


class GeocodeApi:
    url = 'a'

    def get_to_yandex_geo_code(self, cord: str) -> dict:
        response = r.get(self.url)

        if response.status_code == 200:
            print('Ok')
            return json.load(response.raw)
        elif response.status_code == 400:
            print('error format')
        elif response.status_code == 500:
            print('internal server error')
