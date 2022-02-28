from django import forms    # 专门用来存放各种与表单有关的类
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):  # forms.ModelForm跟forms.Form有区别，要对数据库进行修改或写入则用forms.ModelForm，反之
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:  # class Meta做为嵌套类，主要目的是给上级类添加一些功能，或者指定一些标准.
        model = User  # 表示数据写入名为User的数据库表
        fields = ("username", "email")

    def clean_password2(self):
        cd = self.cleaned_data  # cleaned_data是实例的属性，以字典的形式返回实例的具体数据，
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords do not match.")
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "birth")


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "company", "profession", "address", "aboutme", "photo")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)