from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import VoteInfo
from django.views.generic import View

# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, 'vote/login.html')
    else:
        username = request.POST.get("username")
        if username == "zzy":
            # 登录成功之后需要将用户相关cookie存储
            res = redirect(reverse('vote:index'))
            # 设置cookit完成登录
            # res.set_cookie("username", username)
            # 通过session完成登录
            request.session["username"] = username
            return res
        else:
            return render(request, 'vote/login.html', {"error": "用户名错误"})

def logout(request):
    res = redirect(reverse('vote:login'))
    # res.delete_cookie("username")
    # 清除session登录信息
    request.session.flush()
    return res


def index(request):
    contex={'username':'zwj'}
    return render(request,"vote/index.html",contex)

def list(request):
    allvote=VoteInfo.objects.all()
    contex = {'allvote':allvote}
    return render(request, "vote/list.html", contex)

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




