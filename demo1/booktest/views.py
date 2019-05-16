from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Bookinfo,Heroinfo

# Create your views here.

def index(request):
    # return HttpResponse("index首页")
    #1 加载 得到一个模板
    template=loader.get_template("booktest/index.html")
    #2 构造参数字典
    contex={"username":"zwj"}
    #3 使用模板渲染动态数据
    result=template.render(contex)
    #4 将返回数据给页面
    return HttpResponse(result)

def list(request):
    # 查询所有书籍
    allbook=Bookinfo.objects.all()
    # 加载 得到一个模板
    templ=loader.get_template("booktest/list.html")
    # 使用模板渲染动态数据
    result=templ.render({"allbook":allbook})
    # 将返回数据给页面
    return HttpResponse(result)

def detail(request,id):
    # id代表书的主键，用主键找到这本书
    # return HttpResponse("当前为第%s页"%id)
    book=None
    try:    #获得书名【超链接】的ID  为list页面跳转做准备
        book=Bookinfo.objects.get(pk = id)
    except Exception as e:
        return HttpResponse("没有这本书的信息")
    # 加载 得到一个模板
    templ=loader.get_template("booktest/detail.html")
    # 使用模块渲染数据
    result=templ.render({"book":book})
    # 将数据返回给页面
    return HttpResponse(result)


