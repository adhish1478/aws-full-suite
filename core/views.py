from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MediaFileSerializer
from .models import MediaFile
from django.shortcuts import get_object_or_404

# Create your views here.
class MediaUploadView(APIView):
    def post(self, request):
        serializer= MediaFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MediaDetailView(APIView):
    def get(self, request, pk):
        media = get_object_or_404(MediaFile, pk=pk)
        file_key = media.file.name
        url = media.generate_presigned_url()

        return Response({
            "id": media.id,
            "download_url": url
        })
    