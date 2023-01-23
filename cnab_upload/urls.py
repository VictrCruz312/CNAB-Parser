from django.urls import path
from .views import upload_file, listMovimentation

urlpatterns = [
    path("upload/", upload_file, name="upload"),
    path("listMovimentation/", listMovimentation, name="list"),
]
