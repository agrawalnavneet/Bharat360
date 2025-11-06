import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsfeedback.settings')
django.setup()

from news.models import NewsSource, NewsArticle, Feedback

print("=" * 60)
print("NEWS SOURCES")
print("=" * 60)
sources = NewsSource.objects.all()
for source in sources:
    print(f"ID: {source.id} | Name: {source.name} | Region: {source.region} | Active: {source.is_active}")

print("\n" + "=" * 60)
print("NEWS ARTICLES")
print("=" * 60)
articles = NewsArticle.objects.all()
for article in articles:
    print(f"ID: {article.id} | Title: {article.title[:50]}... | Source: {article.source.name} | Category: {article.category}")

print("\n" + "=" * 60)
print("FEEDBACK")
print("=" * 60)
feedbacks = Feedback.objects.all()
for feedback in feedbacks:
    print(f"ID: {feedback.id} | Article: {feedback.article.title[:30]}... | Rating: {feedback.rating}/5 | User: {feedback.user_name or 'Anonymous'}")

print("\n" + "=" * 60)
print("STATISTICS")
print("=" * 60)
print(f"Total Sources: {NewsSource.objects.count()}")
print(f"Total Articles: {NewsArticle.objects.count()}")
print(f"Total Feedback: {Feedback.objects.count()}")

