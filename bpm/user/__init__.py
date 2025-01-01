from django.db import models

class RoleStatus(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    MODERATOR = 'MODERATOR', 'Moderator'
    GENERAL = 'GENERAL', 'General'
