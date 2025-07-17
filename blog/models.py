from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="文章标题")
    content = models.TextField(verbose_name="文章内容")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "博客文章"
        verbose_name_plural = "博客文章管理"

    def __str__(self):
        return self.title