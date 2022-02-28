from django.contrib import admin
from .models import BlogArticles  # 引入编写数据模型的BlogArticles类


class BlogArticlesAdmin(admin.ModelAdmin):  # 设置超级管理员后台界面显示
    list_display = ('title', 'author', 'publish')
    list_filter = ('publish', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['-publish', 'author']


admin.site.register(BlogArticles, BlogArticlesAdmin)  # 将BlogArticles, BlogArticlesAdmin类注册到admin中
