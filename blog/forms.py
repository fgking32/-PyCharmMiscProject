from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # 关联模型
        fields = ('title', 'content')  # 需填写的字段（也可写 '__all__'）
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),  # 让内容框更高
        }
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # 关联你的文章模型
        fields = ['title', 'content']  # 对应模型中的字段
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),  # 可选：美化输入框
        }