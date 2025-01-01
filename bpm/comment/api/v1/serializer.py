from rest_framework import serializers
from bpm.comment.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "user",
            "comment",
            "username"
        ]

    def get_username(self, obj):
        return obj.user.username