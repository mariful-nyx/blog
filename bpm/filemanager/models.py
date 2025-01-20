from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.URLField()
    image_alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.image_alt_text