from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('blog/', include('blog.urls', namespace='blog')),    # 当浏览器输入http://127.0.0.1:8000/blog/则跳转至blog应用urls中
    path('account/', include('account.urls', namespace='account')),
    path('article/', include('article.urls', namespace='article')),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
]
