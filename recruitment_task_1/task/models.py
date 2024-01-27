from mongoengine import Document, fields


class Parts(Document):
    serial_number = fields.StringField()
    name = fields.StringField()
    description = fields.StringField()
    category = fields.StringField()
    quantity = fields.IntField()
    price = fields.FloatField()
    location = fields.DictField()


class Categories(Document):
    name = fields.StringField()
    parent = fields.StringField()

