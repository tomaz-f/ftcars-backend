from flask_restful import Api
from resources.car_resouce import CarResource


def config_routes(app):
    api = Api()

    api.add_resource(CarResource, '/', '/<int:id>',
                     methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])

    api.init_app(app)
