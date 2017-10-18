from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)


class Message(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Entry(models.Model):
    body = RichTextUploadingField() #RichTextField()


class Post(models.Model):
    content = RichTextField()
