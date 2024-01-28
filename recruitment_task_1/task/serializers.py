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

    def validate(self, attrs):
        """
        Check if any parts are assigned to a category.
        Check if parent category has any sub-categories assigned.
        """
        parts = Parts.objects.filter(category=attrs.get('name'))

        if parts.exists():
            raise ValidationError('Cannot modify category while parts are assigned to it!')
        if Categories.objects.filter(parent=self.instance.name).exists():
            raise ValidationError('Cannot modify parent categories if it has other categories assigned!')

        return attrs
