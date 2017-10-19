from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)


class Message(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
