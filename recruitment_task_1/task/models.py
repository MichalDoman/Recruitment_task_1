from mongoengine import Document, fields


class Parts(Document):
    serial_number = fields.StringField(required=True)
    name = fields.StringField(required=True)
    description = fields.StringField(required=True)
    category = fields.StringField(required=True)
    quantity = fields.IntField(required=True)
    price = fields.FloatField(required=True)
    location = fields.DictField(required=True)


class Categories(Document):
    name = fields.StringField(required=True)
    parent = fields.StringField()

