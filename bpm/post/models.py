from django.db import models
from bpm.base.models import BPMDateTime, BPMSEO
from bpm.user.models import User
from bpm.tag.models import Tag
from bpm.category.models import SubSubCategory
from bpm.filemanager.models import Image



class Post(BPMDateTime, BPMSEO):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    thumbnail = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(SubSubCategory, related_name='category_wise_posts', on_delete=models.CASCADE)
    related_article = models.ManyToManyField('Post', blank=True)

    def __str__(self) -> str:
        return self.title
    


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user') 

    def __str__(self):
        return f"Like by {self.user.username} on {self.post.title}"
    