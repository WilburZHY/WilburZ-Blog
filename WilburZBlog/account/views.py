from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm, UserInfoForm, UserForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, UserInfo
from django.http import HttpResponseRedirect
from django.urls import reverse


def user_login(request):
    if request.method == 'POST':  # 如果获取得到前端发来的请求是发送
        login_form = LoginForm(request.POST)
        if login_form.is_valid():  # 如果前端发来的请求登录表单是有值的(表单包含用户名跟密码)
            cd = login_form.cleaned_data  # cleaned_data是实例的属性，以字典的形式返回实例的具体数据，
            # 像此句就会返回{'password': 'xxx', 'username':'xxx'}
            user = authenticate(username=cd['username'], password=cd['password'])  # 对前端发来的表单数据进行认证，如果认证却有
            # 此用户跟密码对得上，则返回值，没通过认证则返回空值
            if user:  # 如果却有此人
                login(request, user)  # 则登录进去
                return HttpResponse('Wellcome. You have been authenticated successfully')  # 显示欢迎信息
            else:
                return HttpResponse('Sorry. Your username or password is not right')
        else:
            return HttpResponse('Invalid Login')

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'account/login.html', {'form': login_form})  # 要传入文件中用于渲染呈现的数据, 默认是字典格式


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponseRedirect(reverse("account:user_login"))
        else:
            return HttpResponse("sorry, you can not register")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {"form": user_form, "profile": userprofile_form})


@login_required()
def myself(request):
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user, 'userprofile') else \
        UserProfile.objects.create(user=request.user)

    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user, 'userinfo') else \
        UserInfo.objects.create(user=request.user)

    return render(request, "account/myself.html",
                  {"user": request.user, "userinfo": userinfo, "userprofile": userprofile})


@login_required(login_url='/account/login/')
def myself_edit(request):
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user, 'userprofile') else \
        UserProfile.objects.create(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user, 'userinfo') else \
        UserInfo.objects.create(user=request.user)

    if request.method == "POST":
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid() * userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            request.user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            request.user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my-information')
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={"birth": userprofile.birth, "phone": userprofile.phone})
        userinfo_form = UserInfoForm(initial={"school": userinfo.school, "company": userinfo.company,
                                              "profession": userinfo.profession, "address": userinfo.address,
                                              "aboutme": userinfo.aboutme})
        return render(request, "account/myself_edit.html", {"user_form": user_form,
                                                            "userprofile_form": userprofile_form,
                                                            "userinfo_form": userinfo_form})


@login_required(login_url='/account/login/')
def my_image(request):
    if request.method == 'POST':
        img = request.POST['img']
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse("1")
    else:
        return render(request, 'account/imagecrop.html',)