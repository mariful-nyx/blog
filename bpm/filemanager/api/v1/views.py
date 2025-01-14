from rest_framework import viewsets
from bpm.filemanager.models import Image
from bpm.filemanager.api.v1.serializers import ImageSerializer



class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer