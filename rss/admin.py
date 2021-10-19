from django.contrib import admin

from rss.models import Article, Vote
from django.db.models import Count

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "link", "user", "created_at", "vote_count"]

    def vote_count(self, obj):
        return obj._vote_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _vote_count=Count("vote", distinct=True),
        )
        return queryset

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ["user", "article"]
    
