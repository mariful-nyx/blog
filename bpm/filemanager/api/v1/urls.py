from rest_framework.routers import DefaultRouter
from bpm.filemanager.api.v1.views import ImageUploadView
from django.urls import path

router = DefaultRouter()

urlpatterns = [
    path('images/', ImageUploadView.as_view(), name='image-upload-view')
]

