from django.urls import path
from bpm.category.api.v1 import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'categories', views.CategoryModelViewSet)

urlpatterns = router.urls

