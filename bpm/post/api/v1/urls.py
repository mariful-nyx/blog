from django.urls import path, include
from bpm.post.api.v1 import views as post_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'posts', post_views.PostsViewSet, basename='post')

urlpatterns = router.urls

urlpatterns += [
    path('post-create/', post_views.PostCreateView.as_view(), name='post-create')
]
