from django import views
from django.urls import path
from newspaper import views

urlpatterns = [
    path('', views.NewsView.as_view()),
    path('create/', views.NewsCreate.as_view()),
    path('news/<int:news_id>/', views.NewsDetail.as_view()),
    path('news/<int:news_id>/add_comment/', views.CommentCreate.as_view()),
    path('news/<int:news_id>/edit/', views.NewsEdit.as_view())
]
