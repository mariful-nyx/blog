from rest_framework.routers import DefaultRouter
from bpm.filemanager.api.v1.views import ImageViewSet

router = DefaultRouter()

router.register(r'images', ImageViewSet)

urlpatterns = router.urls
