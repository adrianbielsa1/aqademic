from django.conf.urls import url
from django.urls import path
from .views import StudentsByFileAPIView, StudentsByNamesAPIView


urlpatterns = [
    path("by-file/<int:expectedFile>/", StudentsByFileAPIView.as_view()),
    path("by-names/<str:expectedNames>/", StudentsByNamesAPIView.as_view()),
]
