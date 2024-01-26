from djongo import models


class Parts(models.Model):
    serial_number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    location = models.JSONField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_name = models.CharField(max_length=255, null=True
                                   )
