from django.contrib import admin
from django.urls import path
from task.views import PartsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PartsListView.as_view(), name='part_list'),
]
