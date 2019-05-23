from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from .models import Article,Category,Tag,MessageInfo
import markdown
from comment. forms import CommentForm
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

    # latestarticle=Article.objects.all().order_by('-create_time')[:3]

    return render(request,'index.html',{'page':page})

def detail(request,id):
    article=get_object_or_404(Article,pk=id)
    article.views+=1
    # 确保body字段还没有更改   不然会报错
    article.save()
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
    cf=CommentForm()
    # latestarticle = Article.objects.all().order_by('-create_time')[:3]
    return render(request,'single.html',locals())

def archives(request,year,month):
    articles=Article.objects.filter(create_time__year=year,create_time__month=month)
    paginator = Paginator(articles, 1)
    # 传入页码   得到页面    page包含所有信息
    page = paginator.get_page(1)
    return render(request, 'index.html', {'page': page})

def category(request,id):
    articles=get_object_or_404(Category,pk=id).article_set.all()
    paginator = Paginator(articles, 1)
    # 传入页码   得到页面    page包含所有信息
    page = paginator.get_page(1)
    return render(request, 'index.html', {'page': page})

def tag(request,id):
    articles = get_object_or_404(Tag, pk=id).article_set.all()
    paginator = Paginator(articles, 1)
    # 传入页码   得到页面    page包含所有信息
    page = paginator.get_page(1)
    return render(request, 'index.html', {'page': page})

def contactus(request):
    return render(request,'contact.html')

def addsuggest(request):
    if request.method == 'POST':
        username=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        info=request.POST.get('message')

        suggest=MessageInfo()

        suggest.username=username
        suggest.email=email
        suggest.subject=subject
        suggest.info=info

        suggest.save()
        return redirect(reverse('#'))


















