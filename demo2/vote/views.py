from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import VoteInfo,MyUser
from django.views.generic import View
from django.contrib.auth import authenticate,login as lgi,logout as lgo
from .util import checklogin
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives
from PIL import Image,ImageDraw,ImageFont
import random,os,io
# 引入序列化加密
from itsdangerous import TimedJSONWebSignatureSerializer as Tjws,SignatureExpired

# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request,'vote/login.html')
    else:
        username=request.POST.get('login_name')
        pwd=request.POST.get('login_pwd')
        verifycode=request.POST.get('verify')
        if verifycode==request.session.get('verifycode'):
            # user=authenticate(request,username=username,password=pwd)
            user = get_object_or_404(MyUser, username=username)
            if not user.is_active:
                return render(request, 'vote/login.html', {"error": "用户尚未激活"})
            else:
                check = user.check_password(pwd)
                if check:
                    lgi(request, user)
                    print(check, '????????')
                    return redirect(reverse('vote:index'))
                else:
                    return render(request, 'vote/login.html', {"error": "用户名或密码错误"})
        else:
            return render(request,'vote/login.html',{'error':'验证码错误'})

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
            url='<a href='+"http:127.0.0.1:8000/vote/active/%s/"%(user.id)+'>点击激活</a>'
            #
            # send_mail('激活账号',url,settings.DEFAULT_FROM_EMAIL,[email])
            # 加密激活地址   加入有效期的序列化
            # de得到序列化工具
            serutil=Tjws(settings.SECRET_KEY,expires_in=600)
            # 使用序列化工具对字典序列化    加密
            result=serutil.dumps({"userid":user.id}).decode("utf-8")
            print(result,type(result),'_____________________________________')
            # try:
            #     obj=serutil.loads(result)
            #     print("________________",obj['userid'],"________")
            # except SignatureExpired as e:
            #     return HttpResponse('验证过期')

            mail=EmailMultiAlternatives('激活账号','<a href=http://127.0.0.1:8000/vote/active/%s/>点击激活</a>'%(result),settings.DEFAULT_FROM_EMAIL,[email])
            mail.content_subtype='html'
            mail.send()
            return render(request,'vote/login.html',{"error":"请在一小时之内激活"})
def active(request,info):
    serutil = Tjws(settings.SECRET_KEY, expires_in=600)
    try:
        obj = serutil.loads(info)
        print("________________", obj['userid'], "________")
        id=obj["userid"]

        user = get_object_or_404(MyUser, pk=id)
        user.is_active = True
        user.save()
        return redirect(reverse('vote:login'))
    except SignatureExpired as e:
        return HttpResponse('验证过期')

def verify(request):
    # 构造动态的验证码，用pillow构造图像，并返回前端页面
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 40
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        # 随机取得位置
        xy = (random.randrange(0, width), random.randrange(0, heigth))
    #     随机取得颜色
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
    # 填充小点
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    print(rand_str)
    # 构造字体对象
    # font = ImageFont.truetype('SCRIPTBL.TTF', 23)
    # fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    # draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    # draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    # draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    # draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    draw.text((5, 2), rand_str[0])
    draw.text((25, 2), rand_str[1])
    draw.text((50, 2), rand_str[2])
    draw.text((75, 2), rand_str[3])
    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')


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
        print(vote.id, "____________________________--")
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



