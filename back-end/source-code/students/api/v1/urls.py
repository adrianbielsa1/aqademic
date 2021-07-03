from django.conf.urls import url
from django.urls import path
from .views import create, delete_by_file, read_by_file, read_by_names


urlpatterns = [
    path("create/", create),
    path("delete/by-file/", delete_by_file),

    path("by-file/<int:expected_file>/", read_by_file),
    path("by-names/<str:expected_names>/", read_by_names),
]
