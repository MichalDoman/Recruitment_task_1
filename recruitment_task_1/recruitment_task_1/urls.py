from django.contrib import admin
from django.urls import path
from task.views import PartsListView, CategoriesListView, CreatePartView, ManagePartView, CategoryPartView, \
    ManageCategoryView, SearchPartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PartsListView.as_view(), name='part-list'),
    path('categories/', CategoriesListView.as_view(), name='categories-list'),
    path('create_part/', CreatePartView.as_view(), name='create-part'),
    path('manage_part/<str:serial_number>/', ManagePartView.as_view(), name='manage-part'),
    path('create_category/', CategoryPartView.as_view(), name='create-category'),
    path('manage_category/<str:name>/', ManageCategoryView.as_view(), name='manage-category'),
    path('search_part/', SearchPartView.as_view(), name='search-part'),
]
