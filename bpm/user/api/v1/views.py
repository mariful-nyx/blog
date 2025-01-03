from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from bpm.user.models import User
from bpm.user.api.v1.serializers import UserSerializer, UserDetailSerializer, SignUpSerializer, LoginSerializer
from bpm.post.pagination import BPMPagination

from rest_framework import filters as drf_filter
from django_filters import rest_framework as filters
import django_filters
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

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

class UserViewSet(UserFilterMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = BPMPagination
    lookup_field = 'username'

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        else:
            return UserSerializer
        

class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    queryset = User.objects.all()


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(username=email, password=password) 
            
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': {
                        'id': user.id,
                        'email': user.email,
                        'username': user.username
                    }
                })
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
