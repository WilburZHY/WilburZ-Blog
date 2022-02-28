from django.shortcuts import render, get_object_or_404
from .models import BlogArticles


def blog_title(request):
    blogs = BlogArticles.objects.all()
    # 将数据渲染到指定模板上。
    # 第1个参数必须是request
    # 然后是模板位置和所传达的数据。
    # 数据是用字典形式传达给模板的。
    return render(request, 'blog/titles.html', {'blogs': blogs})


def blog_article(request, article_id):
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, 'blog/content.html', {'article': article, 'publish': pub})
