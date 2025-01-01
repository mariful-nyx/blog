from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import filters as drf_filter
from django_filters import rest_framework as filters

# Your Models and Serializers
from bpm.post.models import Post
from bpm.post.api.v1.serializers import PostSerializer, PostCreateSerializer, PostDetailSerializer
from bpm.post.pagination import BPMPagination
from bpm.user.api.v1.serializers import UserSerializer  # if needed for your serializer method

# Django Filter for filtering data
import django_filters


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='iexact')
    description = filters.CharFilter(field_name='description', lookup_expr='iexact')
    first_name = filters.CharFilter(field_name='user__first_name', lookup_expr='iexact')
    last_name = filters.CharFilter(field_name='user__last_name', lookup_expr='iexact')
    username = filters.CharFilter(field_name='user__username', lookup_expr='iexact')
    created_at = filters.DateFromToRangeFilter(field_name='created_at')
    updated_at = filters.DateFromToRangeFilter(field_name='updated_at')
    category = filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', 
                  'description', 
                  'first_name', 
                  'last_name', 
                  'username', 
                  'created_at', 
                  'updated_at', 
                  'category'
                  ]


class PostFilterMixin:
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        drf_filter.SearchFilter,
        drf_filter.OrderingFilter
    ]
    search_fields = ['title', 'description', 'user__first_name', 'user__last_name', 'user__username', 'category__name']
    ordering_fields = ['title', 'created_at', 'updated_at']
    filterset_class = PostFilter
    

class PostsViewSet(PostFilterMixin, viewsets.ModelViewSet):
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PostCreateSerializer
        elif self.action == "retrieve":
            return PostDetailSerializer
        return PostSerializer

    def get_queryset(self):
        no_pagination = self.request.query_params.get('all_items')
        if no_pagination:
            self.pagination_class = None
            self.queryset = Post.objects.all()
        else:
            self.pagination_class = BPMPagination
            self.queryset = Post.objects.all()
