from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('article/<int:article_id>/', views.news_detail, name='news_detail'),
    path('article/<int:article_id>/feedback/', views.submit_feedback, name='submit_feedback'),
    path('statistics/', views.statistics, name='statistics'),
]

