from rest_framework import viewsets
from bpm.user.models import User
from bpm.user.api.v1.serializers import UserSerializer, UserDetailSerializer
from bpm.post.pagination import BPMPagination

from rest_framework import filters as drf_filter
from django_filters import rest_framework as filters
import django_filters


class UserFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name='first_name', lookup_expr='icontain')
    last_name = filters.CharFilter(field_name='last_name', lookup_expr='icontain')
    username = filters.CharFilter(field_name='username', lookup_expr='icontain')
    email = filters.CharFilter(field_name='email', lookup_expr='icontain')

    class Meta:
        model = User
        fields = [
                  'first_name', 
                  'last_name', 
                  'username',
                  'email'
                  ]


class UserFilterMixin:
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        drf_filter.SearchFilter,
        drf_filter.OrderingFilter
    ]
    search_fields = ['first_name', 'last_name', 'username', 'email']
    ordering_fields = ['title', 'created_at', 'updated_at']
    filterset_class = UserFilter

class UserViewSet( UserFilterMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = BPMPagination
    lookup_field = 'username'

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        else:
            return UserSerializer