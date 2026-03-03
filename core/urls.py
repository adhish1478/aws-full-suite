from django.urls import path
from .views import MediaUploadView

urlpatterns = [
    path("upload/", MediaUploadView.as_view(), name="upload-file"),
    path("media/<int:pk>/", MediaDetailView.as_view())
]