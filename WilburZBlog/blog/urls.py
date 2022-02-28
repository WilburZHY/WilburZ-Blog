from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_title, name='blog_title'),     # 当跟路由跳转到此应用urls是，则执行views.blog_title函数，渲染至网页
    path('<int:article_id>/', views.blog_article, name='blog_article'),  # 将title.html得到的文章Id传给blog_article函数，从而获得相应点击超链接的文章内容
]