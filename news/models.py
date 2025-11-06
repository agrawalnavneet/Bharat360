from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class NewsSource(models.Model):
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['region', 'name']

    def __str__(self):
        return f"{self.name} ({self.region})"


class NewsArticle(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE, related_name='articles')
    published_date = models.DateTimeField()
    url = models.URLField(blank=True, null=True)
    category = models.CharField(
        max_length=50,
        choices=[
            ('policy', 'Policy'),
            ('legislation', 'Legislation'),
            ('election', 'Election'),
            ('budget', 'Budget'),
            ('public_service', 'Public Service'),
            ('other', 'Other'),
        ],
        default='other'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date', '-created_at']

    def __str__(self):
        return self.title

    def get_feedback_count(self):
        return self.feedback.count()

    def get_average_rating(self):
        feedbacks = self.feedback.all()
        if feedbacks.exists():
            return round(sum(f.rating for f in feedbacks) / feedbacks.count(), 1)
        return None


class Feedback(models.Model):
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE, related_name='feedback')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(blank=True)
    user_name = models.CharField(max_length=100, blank=True)
    user_email = models.EmailField(blank=True)
    is_helpful = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Feedback for {self.article.title} - Rating: {self.rating}"

