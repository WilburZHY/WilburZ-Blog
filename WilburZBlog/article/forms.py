from django import forms
from .models import ArticleColumn, ArticlePost


class ArticleColumnForm(forms.ModelForm):
    class Meta:  # class Meta做为嵌套类，主要目的是给上级类添加一些功能，或者指定一些标准.
        model = ArticleColumn  # 表示数据写入名为ArticleColumn的数据库表
        fields = ("column",)


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ("title", "body")