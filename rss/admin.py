from django.contrib import admin

from rss.models import Article, Vote

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "link", "user", "created_at"]

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ["user", "article"]
    
