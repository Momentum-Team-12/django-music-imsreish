from django.db import models


# Create your models here.
class Album(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    artist = models.CharField(null=True, blank=True, max_length=255)
    album_art = models.ImageField(upload_to='images')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)