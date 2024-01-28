from rest_framework_mongoengine import serializers
from rest_framework.serializers import ValidationError
from .models import Parts, Categories


class PartsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Parts
        fields = "__all__"

    def validate(self, attrs):
        base_categories = [category.parent for category in Categories.objects.all()]

        if attrs.get('category') in base_categories:
            raise ValidationError('Cannot assign base categories')
        if attrs.get('quantity') <= 0:
            raise ValidationError('Quantity cannot be lower than 1')
        if attrs.get('price') < 0:
            raise ValidationError('Price cannot be lower than 0')

        return attrs


class CategoriesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Categories
        fields = "__all__"
