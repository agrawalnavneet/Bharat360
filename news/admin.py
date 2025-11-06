from django.contrib import admin
from .models import NewsSource, NewsArticle, Feedback


@admin.register(NewsSource)
class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'region', 'is_active', 'created_at']
    list_filter = ['region', 'is_active']
    search_fields = ['name', 'region']


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'category', 'published_date', 'get_feedback_count']
    list_filter = ['category', 'source', 'published_date']
    search_fields = ['title', 'content']
    date_hierarchy = 'published_date'
    readonly_fields = ['created_at', 'updated_at']

    def get_feedback_count(self, obj):
        return obj.get_feedback_count()
    get_feedback_count.short_description = 'Feedback Count'


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['article', 'rating', 'is_helpful', 'user_name', 'created_at']
    list_filter = ['rating', 'is_helpful', 'created_at']
    search_fields = ['article__title', 'comment', 'user_name', 'user_email']
    readonly_fields = ['created_at', 'ip_address']
    date_hierarchy = 'created_at'

