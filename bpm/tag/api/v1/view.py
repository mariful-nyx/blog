from rest_framework import generics, viewsets
from bpm.tag.models import Tag
from bpm.tag.api.v1.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None