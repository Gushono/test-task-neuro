class GeocodeApi:
    url = 'a'

    def get_to_yandex_geo_code(self, cord: str) -> dict:
        # response = r.get(self.url)
        response = 'a'

        if response == 'a':
            print('Ok')
            return {'a': 'a'}
        elif response.status_code == 400:
            print('error format')
        elif response.status_code == 500:
            print('internal server error')
