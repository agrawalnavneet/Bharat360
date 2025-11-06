from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Avg, Count
from django.http import JsonResponse
from .models import NewsArticle, NewsSource, Feedback
from .forms import FeedbackForm, NewsFilterForm


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def news_list(request):
    articles = NewsArticle.objects.select_related('source').prefetch_related('feedback').all()
    
    filter_form = NewsFilterForm(request.GET)
    
    region = request.GET.get('region')
    category = request.GET.get('category')
    source_id = request.GET.get('source')
    
    if region:
        articles = articles.filter(source__region__icontains=region)
    if category:
        articles = articles.filter(category=category)
    if source_id:
        articles = articles.filter(source_id=source_id)
    
    regions = NewsSource.objects.values_list('region', flat=True).distinct()
    
    paginator = Paginator(articles, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'filter_form': filter_form,
        'regions': regions,
        'sources': NewsSource.objects.filter(is_active=True),
    }
    
    return render(request, 'news/news_list.html', context)


def news_detail(request, article_id):
    article = get_object_or_404(NewsArticle.objects.select_related('source'), id=article_id)
    
    recent_feedback = article.feedback.all()[:10]
    
    feedback_stats = article.feedback.aggregate(
        avg_rating=Avg('rating'),
        total_count=Count('id')
    )
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.article = article
            feedback.ip_address = get_client_ip(request)
            feedback.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('news_detail', article_id=article.id)
    else:
        form = FeedbackForm()
    
    related_articles = NewsArticle.objects.filter(
        source=article.source
    ).exclude(id=article.id)[:3]
    
    context = {
        'article': article,
        'form': form,
        'recent_feedback': recent_feedback,
        'feedback_stats': feedback_stats,
        'related_articles': related_articles,
    }
    
    return render(request, 'news/news_detail.html', context)


def submit_feedback(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(NewsArticle, id=article_id)
        form = FeedbackForm(request.POST)
        
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.article = article
            feedback.ip_address = get_client_ip(request)
            feedback.save()
            
            return JsonResponse({
                'success': True,
                'message': 'Thank you for your feedback!',
                'rating': feedback.rating,
                'comment': feedback.comment,
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors
            }, status=400)
    
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)


def statistics(request):
    total_articles = NewsArticle.objects.count()
    total_feedback = Feedback.objects.count()
    total_sources = NewsSource.objects.filter(is_active=True).count()
    
    avg_rating = Feedback.objects.aggregate(avg=Avg('rating'))['avg']
    
    articles_by_category = NewsArticle.objects.values('category').annotate(
        count=Count('id')
    ).order_by('-count')
    
    top_sources = NewsSource.objects.annotate(
        article_count=Count('articles')
    ).filter(is_active=True).order_by('-article_count')[:10]
    
    top_articles = NewsArticle.objects.annotate(
        feedback_count=Count('feedback')
    ).filter(feedback_count__gt=0).order_by('-feedback_count')[:10]
    
    context = {
        'total_articles': total_articles,
        'total_feedback': total_feedback,
        'total_sources': total_sources,
        'avg_rating': round(avg_rating, 2) if avg_rating else None,
        'articles_by_category': articles_by_category,
        'top_sources': top_sources,
        'top_articles': top_articles,
    }
    
    return render(request, 'news/statistics.html', context)

