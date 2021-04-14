from django.urls import path, include


urlpatterns = [
    path("api/v1/", include("source-code.students.api.v1.urls")),
]
