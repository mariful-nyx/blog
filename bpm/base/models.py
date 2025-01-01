from django.db import models

class BPMDateTime(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True

class BPMSEO(models.Model):
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract=True


class NameDescAbstract(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        abstract=True