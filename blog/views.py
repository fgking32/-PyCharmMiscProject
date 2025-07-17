from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


# 文章列表视图
def article_list(request):
    article_list = Article.objects.all().order_by('-created_time')
    return render(
        request,
        template_name='blog/article_list.html',
        context={'article_list': article_list}
    )


# 文章详情视图
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(
        request,
        template_name='blog/article_detail.html',
        context={'article': article}
    )


# 文章创建视图（需登录）
@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 保存表单数据到数据库
            article = form.save(commit=False)
            article.author = request.user  # 关联当前登录用户为作者
            article.save()
            return redirect('blog:article_list')  # 跳转回列表页
    else:
        #  GET请求时显示空表单
        form = ArticleForm()

    return render(
        request,
        template_name='blog/article_create.html',
        context={'form': form}
    )
