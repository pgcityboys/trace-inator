from flask_marshmallow import Schema


class PlacesSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["places"]
