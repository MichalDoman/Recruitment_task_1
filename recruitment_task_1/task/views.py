from rest_framework import generics
from task.models import Parts, Categories
from task.serializers import PartsSerializer, CategoriesSerializer


class PartsListView(generics.ListAPIView):
    queryset = Parts.objects.all()
    serializer_class = PartsSerializer

