from __future__ import unicode_literals

from django.db import models

class Thread(models.Model):
    text = models.CharField(max_length=3000)
    document = models.FileField(upload_to='chan/documents/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    text = models.CharField(max_length=3000)
    document = models.FileField(upload_to='chan/documents/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
