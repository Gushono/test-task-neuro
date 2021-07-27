class Coordinates:
    lat: float
    lng: float

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def to_tuple(self):
        """
        Convert a cordinate object to a tuple
        """
        return self.lat, self.lng
