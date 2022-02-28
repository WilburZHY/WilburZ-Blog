from django.db import models
from django.contrib.auth.models import User
from django import forms


class UserProfile(models.Model):  # 建立名为UserProfile的数据库表
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)


class UserInfo(models.Model):  # 针对UserInfo数据模型类
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    school = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    aboutme = models.TextField(blank=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return 'user:{}'.format(self.user.username)


class UserForm(forms.ModelForm):  # 对于来自auth_user(django默认)数据库表的信息，也要写一个表单类来对应
    class Meta:
        model = User
        fields = ("email",)