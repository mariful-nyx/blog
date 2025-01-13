from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bpm.user.api.v1.views import UserViewSet, SignUpView, LoginView, ProtectedView
from rest_framework_simplejwt.views import TokenRefreshView


router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]
