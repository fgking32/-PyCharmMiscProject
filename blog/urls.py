from django.urls import path
from . import views

# 命名空间（必须，模板/视图反向解析用 `blog:xxx`）
from django.urls import path, include  # 统一导入，只写1次
from . import views

app_name = 'blog'  # 命名空间，只写1次

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('create/', views.article_create, name='article_create'),
    path('accounts/', include('django.contrib.auth.urls')),
]