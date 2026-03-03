from django.urls import path
from .views import MediaUploadView, MediaDetailView

urlpatterns = [
    path("upload/", MediaUploadView.as_view(), name="upload-file"),
    path("media/<int:pk>/", MediaDetailView.as_view())
]