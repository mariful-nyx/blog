from rest_framework import serializers
from bpm.user.models import User
from bpm.post.api.v1.serializers import PostSerializer
from bpm.comment.api.v1.serializer import CommentSerializer



class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    avatar_preview = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "avater",
            "avatar_preview",
            "date_joined",
            "role",
            "posts",
            "comments",
            "status",
            "profession",
            "university"
        ]
    
    def get_posts(self, obj):
        return obj.posts.count()
    
    def get_comments(self, obj):
        return obj.comments.count()

    def get_avatar_preview(self, obj):
        if obj.avater:
            return obj.avater.image
        return None
    

class UserDetailSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    avatar_preview = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "avater",
            "avatar_preview",
            "is_staff",
            "is_active",
            "date_joined",
            "last_login",
            "is_superuser",
            "posts",
            "comments",
            "role",
            "status",
            "profession",
            "university"
        ]
    
    def get_avatar_preview(self, obj):
        if obj.avater:
            return obj.avater.image
        return None


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        return user
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)