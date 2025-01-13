from rest_framework import generics, viewsets
from bpm.category.models import Category
from bpm.category.api.v1.seralizers import CategorySerializer, CategoryWithPostsSerializer, CategoryCreateSerializer, SubSubCategorySerializer
from bpm.category.models import SubSubCategory


class CategoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = None

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CategoryWithPostsSerializer
        elif self.action == "post":
            return CategoryCreateSerializer
        else:
            return CategorySerializer
