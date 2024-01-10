from flask_marshmallow import Schema


class TraceSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["paths"]
