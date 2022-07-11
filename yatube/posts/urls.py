from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('posts/', views.posts_list),
    path('posts/<slug:slug>/', views.group_posts),
]
