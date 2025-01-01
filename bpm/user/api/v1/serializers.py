from rest_framework import serializers
from bpm.user.models import User
from bpm.post.api.v1.serializers import PostSerializer
from bpm.comment.api.v1.serializer import CommentSerializer



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "avater",
            "date_joined",
            "role"
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "avater",
            "is_staff",
            "is_active",
            "date_joined",
            "last_login",
            "is_superuser",
            "posts",
            "comments",
            "role"
        ]