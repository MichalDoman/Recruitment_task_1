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


class SearchPartView(generics.ListAPIView):
    serializer_class = PartsSerializer

    def get_queryset(self):
        params = self.request.query_params
        queryset = Parts.objects.all()

        if params.get('serial_number'):
            queryset = queryset.filter(serial_number__icontains=params.get('serial_number'))
        if params.get('name'):
            queryset = queryset.filter(name__icontains=params.get('name'))
        if params.get('description'):
            queryset = queryset.filter(description__icontains=params.get('description'))
        if params.get('category'):
            queryset = queryset.filter(category__icontains=params.get('category'))
        if params.get('quantity'):
            queryset = queryset.filter(quantity__icontains=params.get('quantity'))
        if params.get('price'):
            queryset = queryset.filter(price__icontains=params.get('price'))

        return queryset


