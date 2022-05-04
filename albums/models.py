from django.db import models


# Create your models here.
class Album(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    artist = models.CharField(null=True, blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
