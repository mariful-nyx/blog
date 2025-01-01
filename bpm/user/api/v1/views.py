from rest_framework import viewsets
from bpm.user.models import User
from bpm.user.api.v1.serializers import UserSerializer, UserDetailSerializer
from bpm.post.pagination import BPMPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = BPMPagination
    lookup_field = 'username'

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        else:
            return UserSerializer