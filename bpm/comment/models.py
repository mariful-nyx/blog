from django.db import models
from bpm.user.models import User
from bpm.post.models import Post
from bpm.base.models import BPMDateTime
# Create your models here.


class Comment(BPMDateTime):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self) -> str:
        return self.comment
