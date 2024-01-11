from flask_marshmallow import Schema


class PlacesSchema(Schema):
    class Meta:
        fields = ["places"]
