from django.db import models
from django.contrib.auth.models import AbstractUser
from bpm.user import RoleStatus
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    avater = models.ImageField(upload_to='images', blank=True, null=True)
    role = models.CharField(max_length=20, choices=RoleStatus.choices, default=RoleStatus.GENERAL)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self) -> str:
        return self.first_name + self.last_name