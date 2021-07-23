from flask_restplus import Namespace, Resource, fields
from services.geocode import GeocodeApi

namespace = Namespace('distance', 'Distance of two points')

distance_model = namespace.model('Distance', {
    'distance_in_meters': fields.String(
        readonly=True,
        description='Return de distance in meters between two points'
    )
})

distance_model_exemple = {'distance_in_meters': '100 Meters!'}


@namespace.route('')
class Distance(Resource):

    @namespace.marshal_with(distance_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        """
        This endpoint will return the distance between two points

        :return: An object of Distance
        """

        geocode = GeocodeApi()

        # distance_to = geocode.get_to_yandex_geo_code("312")

        distance_to = 1

        return {"distance_in_meters": 40000}
