from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Article
import markdown
# 分页器
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    pagenum=request.GET.get('page')
    # pagenum=1 if pagenum==None else pagenum
    if pagenum==None:
        pagenum=1
    else:
        pagenum=pagenum
    articles=Article.objects.all().order_by('-views')
    print(pagenum)
    paginator=Paginator(articles,1)
    # 传入页码   得到页面    page包含所有信息
    page=paginator.get_page(pagenum)

    return render(request,'index.html',{'page':page})

def detail(request,id):
    article=get_object_or_404(Article,pk=id)
    # 处理body
    # 使用makedown 处理数据    将makedown语法转换为HTML标签
    # article.body=markdown.markdown(article.body,extensions=[
    #     'markdown.extensions.extra',
    #     'markdown.extensions.codehilite',
    #     'markdown.extensions.toc'
    #     ])

    # 方法2 外部使用目录  需要使用构造函数的写法
    mk=markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
        ])
    article.body=mk.convert(article.body)
    # 把makedown中的目录赋予TOC
    article.toc=mk.toc

    return render(request,'single.html',locals())
