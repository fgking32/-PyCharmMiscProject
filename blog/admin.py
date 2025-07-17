from django.contrib import admin
from .models import Article

@admin.register(Article)  # 装饰器注册（保留这一个）
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'id')
    search_fields = ('title',)
    ordering = ('-created_time',)
    fields = ('title', 'content')  # 显示可修改的字段（按需添加）