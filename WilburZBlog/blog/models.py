from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:  # 主要目的是给上级类添加一些功能，或者指定一些标准
        ordering = ('-publish',)

    def __str__(self):  # 得到想要的易于人阅读的对象的信息
        return self.title
