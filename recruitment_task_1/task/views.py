from rest_framework_mongoengine import generics
from task.models import Parts, Categories
from task.serializers import PartsSerializer, CategoriesSerializer


class PartsListView(generics.ListAPIView):
    queryset = Parts.objects.all()
    serializer_class = PartsSerializer


class CategoriesListView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CreatePartView(generics.CreateAPIView):
    queryset = Parts.objects.all()
    serializer_class = PartsSerializer


class ManagePartView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parts.objects.all()
    serializer_class = PartsSerializer
    lookup_field = "serial_number"


class CategoryPartView(generics.CreateAPIView):
    queryset = Categories
    serializer_class = CategoriesSerializer


class ManageCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    lookup_field = "name"
