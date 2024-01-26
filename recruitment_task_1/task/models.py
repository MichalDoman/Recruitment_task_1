from mongoengine import Document, fields, CASCADE


class Parts(Document):
    serial_number = fields.StringField(max_length=255, primary_key=True)
    name = fields.StringField(max_length=255)
    description = fields.StringField()
    category = fields.StringField(max_length=255)
    quantity = fields.IntField()
    price = fields.FloatField()
    location = fields.DictField()


class Category(Document):
    name = fields.StringField()
    parent = fields.ReferenceField('Category', reverse_delete_rule=CASCADE)

