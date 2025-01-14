from bpm.tag.api.v1.view import TagViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'tags', TagViewSet)

urlpatterns = router.urls

