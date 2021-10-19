from os import link
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group


class Article(models.Model):
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=512, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return f"Vote '{self.article}'"

class Site(models.Model):
    link = models.CharField(max_length=200)
    def __str__(self):
        return f"Vote '{self.link}'"
