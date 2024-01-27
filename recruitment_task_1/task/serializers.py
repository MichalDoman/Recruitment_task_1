from rest_framework_mongoengine import serializers
from .models import Parts, Categories


class PartsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Parts
        fields = "__all__"


class CategoriesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Categories
        fields = "__all__"
