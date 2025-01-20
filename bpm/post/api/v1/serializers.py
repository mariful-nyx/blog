from rest_framework import serializers
from bpm.post.models import Post
from bpm.category.api.v1.seralizers import CategorySerializer
from bpm.tag.api.v1.serializers import TagSerializer
from bpm.tag.models import Tag
from bpm.category.models import SubSubCategory
from bpm.user.models import User
from django.db import transaction



class PostSerializer(serializers.ModelSerializer):
    posted_by = serializers.SerializerMethodField()
    thumbnail_img = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'posted_by',
            'thumbnail',
            'thumbnail_img',
            'title',
            'description',
            'created_at',
            'updated_at',
            'slug',
        ]

    def get_posted_by(self, obj):
        return obj.user.username
    
    def get_thumbnail_img(self, obj):
        request = self.context.get('request')

        if obj.thumbnail:
            return obj.thumbnail.image
        return None


class PostDetailSerializer(serializers.ModelSerializer):

    tag = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    liked_users = serializers.SerializerMethodField()
    posted_by = serializers.SerializerMethodField()
    related_article = PostSerializer(many=True, read_only=True)
    thumbnail_img = serializers.SerializerMethodField()

    class Meta:
        model = Post
        
        fields = [
            'id',
            'user',
            'posted_by',
            'thumbnail',
            'thumbnail_img',
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
    
    def get_thumbnail_img(self, obj):
        request = self.context.get('request')

        if obj.thumbnail:
            return obj.thumbnail.image.url
        return None
    


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
            'meta_title',
            'meta_description',
            'slug',
            'related_article',
        ]
    
    def create(self, validated_data):

        tags = validated_data.pop('tag', [])
        related_articles = validated_data.pop('related_article', [])

        with transaction.atomic():
            post = Post.objects.create(**validated_data)
            post.tag.set(tags)
            post.related_article.set(related_articles)
            post.save()

        return post
