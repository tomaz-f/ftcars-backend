from marshmallow import Schema, fields


class CarSchema(Schema):
    id = fields.Int()
    brand = fields.Str(required=True)
    name = fields.Str(required=True)
    year = fields.Int(required=True)
    color = fields.Str(required=True)
    type = fields.Str(required=True)


car_schema = CarSchema()
cars_schema = CarSchema(many=True)
