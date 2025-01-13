from rest_framework import serializers
from bpm.post.models import Post
from bpm.category.api.v1.seralizers import CategorySerializer
from bpm.tag.api.v1.serializers import TagSerializer
from bpm.tag.models import Tag
from bpm.category.models import SubSubCategory


class PostSerializer(serializers.ModelSerializer):
    posted_by = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'posted_by',
            'thumbnail',
            'title',
            'description',
            'created_at',
            'updated_at',
            'slug',
        ]

    def get_posted_by(self, obj):
        return obj.user.username


class PostDetailSerializer(serializers.ModelSerializer):

    tag = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    liked_users = serializers.SerializerMethodField()
    posted_by = serializers.SerializerMethodField()
    related_article = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        
        fields = [
            'id',
            'user',
            'posted_by',
            'thumbnail',
            'title',
            'description',
            'tag',
            'category',
            'likes_count',
            'liked_users',
            'created_at',
            'updated_at',
            'meta_title',
            'meta_description',
            'slug',
            'related_article'
        ]

    def get_liked_users(self, obj):

        likes = obj.likes.all()
        users = [like.user for like in likes]

        likes_user_data = []

        for user in users:
            likes_user_data.append({
                'id': user.id,
                'username': user.username,
                'email': user.email
            })

        return likes_user_data
    
    def get_posted_by(self, obj):
        return obj.user.username
    


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'thumbnail',
            'title',
            'description',
            'tag',
            'category',
            'created_at',
            'updated_at',
            'meta_title',
            'meta_description',
            'slug',
        ]
        read_only_fields = ['user']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user

        tag_payload = validated_data['tag']
        category_payload = validated_data['category']
        tags = []

        for tag in tag_payload:
            tag_instance = Tag.objects.create(
                name=tag
            )
            tags.append(tag_instance)

        validated_data['tag'] = tags
        category_instance = SubSubCategory.objects.get(category_payload)
        validated_data['category'] = category_instance

        return super().create(validated_data)
       