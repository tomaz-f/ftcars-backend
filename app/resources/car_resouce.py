from flask_restful import Resource
from flask import request
from schemas.car_schema import car_schema, cars_schema
from conn_db import db
from models.car_model import Car


class CarResource(Resource):
    def get(self, id=None):
        if id:
            car = Car.query.get(id)
            if not car:
                return {'message': 'Car not found'}, 404

            result = car_schema.dump(car)
            return {'status': 'Success', 'data': result}, 200

        cars = Car.query.all()
        result = cars_schema.dump(cars)
        return {'status': 'Success', 'data': result}, 200

    def post(self):
        # a function that create a new car in database,
        # and return a json with the new car created
        # must not receive this erro: TypeError: tuple indices must be integers or slices, not str

        json_data = request.get_json()
        if not json_data:
            return {'message': 'Expected a json, but receive None'}, 400

        data = car_schema.load(json_data)
        if isinstance(data, tuple):
            data = data[0]
        car = Car(**data)
        db.session.add(car)
        db.session.commit()
        result = car_schema.dump(car)
        return {'status': 'Success', 'data': result}, 201

    def put(self, id):
        json_data = request.get_json()
        if not json_data:
            return {'message': 'Expected a json, but receive None'}, 400

        data = car_schema.load(json_data)
        car = Car.query.get(id)
        if not car:
            return {'message': 'Car not found'}, 404

        car.brand = data['brand']
        car.name = data['name']
        car.year = data['year']
        car.color = data['color']
        car.type = data['type']

        db.session.commit()
        result = car_schema.dump(car)
        return {'status': 'Success', 'data': result}, 204

    def patch(self, id):
        carro = Car.query.get(id)
        if not carro:
            return {'message': 'Car not found'}, 404

        json_data = request.get_json()
        if not json_data:
            return {'message': 'Expected a json, but receive None'}, 400

        data = car_schema.load(json_data, partial=True)
        for key, value in data.items():
            setattr(carro, key, value)

        db.session.commit()
        result = car_schema.dump(carro)

        return {'status': 'Success', 'data': result}, 204

    def delete(self, id):
        car = Car.query.get(id)
        db.session.delete(car)
        db.session.commit()

        return {'message': 'Car deleted.'}, 204
