from datetime import datetime
from os import link, times
from django.shortcuts import render
import feedparser
from django.http import HttpResponse
from feedparser import datetimes
import requests
from dateutil.easter import *
from dateutil.relativedelta import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *
from django.utils import timezone
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rss.models import Article, Site
from rss.serializers import UserSerializer, GroupSerializer, ArticleSerializer
from django.db import IntegrityError


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        self.searchArticle()
        return super().list(request, args, kwargs)
        
        
    def searchArticle(self):
        for site in Site.objects.all():
            parsed_article = feedparser.parse(site.link)
            if hasattr(parsed_article.feed, 'published'):
                date = parse(parsed_article.feed.published).date()
            else:
                date = timezone.now()
            article = Article(title=parsed_article.feed.title, 
            link=parsed_article.feed.link, created_at=date)
            try:
                article.save()
            except IntegrityError as e:
                pass


              






 






