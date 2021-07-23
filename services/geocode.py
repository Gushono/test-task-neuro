import json
from dataclasses import dataclass
import requests as r
from requests import Response


@dataclass
class GeocodeApi:
    api_key: str
    url: str = "randex"

    def get_to_yandex_geo_code(self, cord: str) -> dict:
        response = r.get(self.url)

        if response.status_code == 200:
            print('Ok')
            return json.load(response.raw)
        elif response.status_code == 400:
            print('error format')
        elif response.status_code == 500:
            print('internal server error')
