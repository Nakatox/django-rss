from django.contrib import admin

from rss.models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "link", "user", "created_at"]
    
