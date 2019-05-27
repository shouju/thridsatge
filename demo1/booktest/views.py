from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Bookinfo,Heroinfo

# Create your views here.

def index(request):
    # return HttpResponse("index首页")
    #1 加载 得到一个模板
    # template=loader.get_template("booktest/index.html")
    #2 构造参数字典
    # contex={"username":"zwj"}
    #3 使用模板渲染动态数据
    # result=template.render(contex)
    #4 将返回数据给页面
    # return HttpResponse(result)
    # -----------------render简写------------------------
    contex = {"username": "zwj"}
    return render(request,"booktest/index.html",contex)
def list(request):
    # 查询所有书籍
    # allbook=Bookinfo.objects.all()
    # 加载 得到一个模板
    # templ=loader.get_template("booktest/list.html")
    # 使用模板渲染动态数据
    # contex = {"allbook":allbook}
    # result=templ.render({"allbook":allbook})
    # 将返回数据给页面
    # return HttpResponse(result)

    # -----------------render简写------------------------
    allbook = Bookinfo.objects.all()
    contex = {"allbook": allbook}
    return render(request,"booktest/list.html",contex)
def detail(request,id):
    # id代表书的主键，用主键找到这本书
    # return HttpResponse("当前为第%s页"%id)
    # book=None
    # try:    #获得书名【超链接】的ID  为list页面跳转做准备
    #     book=Bookinfo.objects.get(pk = id)
    # except Exception as e:
    #     return HttpResponse("没有这本书的信息")
    # 加载 得到一个模板
    # templ=loader.get_template("booktest/detail.html")
    # 使用模块渲染数据
    # result=templ.render({"book":book})
    # 将数据返回给页面
    # return HttpResponse(result)
    # -----------------render简写------------------------
    book=Bookinfo.objects.get(pk = id)
    context={"book":book}
    return render(request,"booktest/detail.html",context)

def deletebook(request,id):
    # return HttpResponse("success")
    # 删除英雄   通过书名的id删除
    Bookinfo.objects.get(pk=id).delete()
    # 返回已删除的书籍列表页面
    return HttpResponseRedirect(redirect_to="/booktest/list/")

def deletehero(request,id):
    # return HttpResponse("success")
    # 通过id获取永雄
    hero=Heroinfo.objects.get(pk=id)
    # 通过英雄获取书籍的id
    bookid=hero.book.id
    # 删除英雄
    hero.delete()
    # 返回已删除后英雄的界面         通过书籍的id进入该书籍的已删除的英雄列表
    return HttpResponseRedirect(redirect_to="/booktest/detail/%s/"%(bookid))

def addhero(request,id):
    # return HttpResponse("添加
    if request.method=="GET":
        return render(request,"booktest/addhero.html",{"bookid":id})
    elif request.method=="POST":
        book=Bookinfo.objects.get(pk=id)
        hero=Heroinfo()
        hero.name=request.POST["username"]
        value=request.POST["sex"]
        hero.gendle=value
        hero.skill=request.POST["skill"]
        hero.book=book
        hero.save()
        return HttpResponseRedirect("/booktest/detail/%s/"%(id,))

def updatehero(request,id):
    hero=Heroinfo.objects.get(pk=id)
    if request.method=="GET":
        return render(request,"booktest/updatehero.html",{"hero":hero})

    elif request.method=="POST":
        hero.name = request.POST["username"]
        hero.gendle= request.POST["sex"]
        hero.skill = request.POST["skill"]
        hero.save()
        return HttpResponseRedirect("/booktest/detail/%s/"%(hero.book.id))

def addbook(request):
    if request.method=="GET":
        return render(request,"booktest/addbook.html")
    elif request.method=="POST":
        print('post')
        book=Bookinfo()
        book.title=request.POST["bid"]
        book.pub_date=request.POST["time"]
        book.save()
        return HttpResponseRedirect("/booktest/list/")

def updatebook(request,id):
    book=Bookinfo.objects.get(pk=id)
    if request.method=="GET":
        return render(request,"booktest/updatebook.html",{"bookid":id})
    elif request.method=="POST":
        book.title = request.POST["bid"]
        book.pub_date = request.POST["time"]
        book.save()
        return HttpResponseRedirect("/booktest/list/")
    # return HttpResponse("修改成功")


        # return HttpResponse("添加成功")










