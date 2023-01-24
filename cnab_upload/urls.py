from django.urls import path
from .views import UploadFileView, ItemListView

urlpatterns = [
    path("upload/", UploadFileView.as_view(), name="upload"),
    path("upload/listMovimentation/", ItemListView.as_view(), name="list"),
]
