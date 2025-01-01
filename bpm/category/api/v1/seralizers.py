from rest_framework import serializers
from bpm.category.models import Category, SubCategory, SubSubCategory


class SubSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSubCategory
        fields = ['id', 'name', 'description']

class SubCategorySerializer(serializers.ModelSerializer):
    subsubcategories = SubSubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'description', 'subsubcategories']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'subcategories']



class CategoryWithPostsSerializer(serializers.ModelSerializer):

    category_wise_posts = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "category_wise_posts"
        ]

    def get_category_wise_posts(self, obj):
        posts = obj.category_wise_posts.all()

        category_posts = []
        request = self.context.get('request')

        for post in posts:
         
            category_posts.append({
                "id": post.id,
                "thumbnail": request.build_absolute_uri(post.thumbnail.url) if post.thumbnail else None, 
                "title": post.title,
                "slug": post.slug,
                "updated_at": post.updated_at,
                "created_at": post.created_at,
                "posted_by": post.user.username
            })

        return category_posts





class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        pass