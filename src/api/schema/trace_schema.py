from flask_marshmallow import Schema


class TraceSchema(Schema):
    class Meta:
        fields = ["paths"]
