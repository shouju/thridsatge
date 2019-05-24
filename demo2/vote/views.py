from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import VoteInfo,MyUser
from django.views.generic import View
from django.contrib.auth import authenticate,login as lgi,logout as lgo
from .util import checklogin
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request,'vote/login.html')
    else:
        username=request.POST.get('login_name')
        pwd=request.POST.get('login_pwd')
        # user=authenticate(request,username=username,password=pwd)
        user=get_object_or_404(MyUser,username=username)
        if not user.is_active:
            return render(request, 'vote/login.html', {"error": "用户尚未激活"})
        else:
            check=user.check_password(pwd)
            if check:
                lgi(request, user)
                print(check, '????????')
                return redirect(reverse('vote:index'))
            else:
                return render(request, 'vote/login.html', {"error": "用户名或密码错误"})
    # if user:
    #     if user.is_active:
    #         lgi(request,user)
    #         return redirect(reverse('vote:index'))
    #     else:
    #         return render(request, 'vote/login.html', {"error": "用户尚未激活"})
    # # return HttpResponseRedirect(request,'/vote/index/%s'%(id,))
    # else:
    #     error=None
    #     error="用户名或者密码错误"
    #     return render(request,'vote/login.html',{"error":error})
    # if request.method == "GET":
    #     return render(request, 'vote/login.html')
    # else:
    #     username = request.POST.get("username")
    #     if username == "zzy":
    #         # 登录成功之后需要将用户相关cookie存储
    #         res = redirect(reverse('vote:index'))
    #         # 设置cookit完成登录
    #         # res.set_cookie("username", username)
    #         # 通过session完成登录
    #         request.session["username"] = username
    #         return request
    #     else:
    #         return render(request, 'vote/login.html', {"error": "用户名错误"})

def logout(request):
    res = redirect(reverse('vote:login'))
    request.session.flush()
    return res

def register(request):

    if request.method=='POST':
        username=request.POST.get('regis_name')
        pwd=request.POST.get('regis_pwd')
        pwd2 = request.POST.get('regis_pwd1')
        email=request.POST.get('email')
        print(username,pwd,pwd2)
        error=None
        if pwd!=pwd2:
            error = "密码不一致"
            return render(request,'vote/login.html',{"error":error})
        else:
            user=MyUser.objects.create_user(username=username,password=pwd)
            print(user.id,user.is_active)
            user.is_active=False
            user.save()

            return redirect(reverse('vote:login'))

def change_pwd(request):
    if request.method=="GET":
        return render(request,'vote/change_pwd.html',locals())

@checklogin
def index(request):
    user=request.POST.get('username')
    # username = request.session.get('username')
    questions = VoteInfo.objects.all()
    return render(request,'vote/index.html', locals())

@checklogin
def index(request):
    # contex={'username':'zwj'}
    contex={}
    return render(request,"vote/index.html",contex)

@checklogin
def list(request):
    allvote=VoteInfo.objects.all()
    contex = {'allvote':allvote}
    return render(request, "vote/list.html", contex)

@checklogin
def detail(request,id):
    vote=VoteInfo.objects.get(pk=id)
    contex = {"vote": vote}
    if request.method == "GET":
        return render(request, "vote/detail.html", contex)
    elif request.method == "POST":
        x = request.POST['choose']
        x=int(x)
        print(x,type(x))
        if x==1:
            vote.choose1vote+=1
        else:
            vote.choose2vote+=1
        vote.save()
        print(vote.id, "_________________________--")
        return HttpResponseRedirect('/vote/result/%s/'%(id,))

@checklogin
def result(request, id):
    vote = VoteInfo.objects.get(pk=id)
    # print(vote.id,'__________________________________')
    c = {'vote': vote}
    return render(request, "vote/result.html",c)
    # return HttpResponse('ok-Ok-OK')

    # vote.matter=VoteInfo.objects.get(vote.matter)
    # print(vote.matter)
    # vote.choose1 = VoteInfo.objects.get(vote.choose1)
    # vote.choose2 = VoteInfo.objects.get(vote.choose2)
    # vote.choose1vote = VoteInfo.objects.get(vote.choose1vote)
    # vote.choose2vote = VoteInfo.objects.get(vote.choose2vote)
    # return render(request, "vote/result.html/%s/"%(id,))

def suggest(request):
    return redirect(reverse('vote:suggest'))



