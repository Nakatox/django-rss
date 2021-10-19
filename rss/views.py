from django.shortcuts import render
import feedparser
from django.http import HttpResponse
import requests

def parser(request) :
    # link rss : view-source:https://daily.dev/blog
    d = feedparser.parse(requests.get("https://www.clubic.com/feed/news.rss").text)
    return HttpResponse(str(d['entries'][0]))
