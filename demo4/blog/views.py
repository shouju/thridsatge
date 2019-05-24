from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from .models import Article,Category,Tag,MessageInfo,Ads
import markdown
from comment. forms import CommentForm
from django.views.generic import View
# 分页器
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
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

class Contacts(View):
    def get(self,request):
        cf=CommentForm()
        return render(request, 'contact.html',locals())

    def post(self,request):
        # return HttpResponse('fasong')

        from django.conf import settings
        send_mail("Django邮件0", "Django可以发送邮件", settings.DEFAULT_FROM_EMAIL, ["1120648012@qq.com",'shoujut163.com'])
        return redirect(reverse('blog:contactus'))


class Adds(View):
    def get(self,request):
        return render(request,'addads.html')

    def post(self,request):
        img=request.FILES['img']
        desc=request.POST.get('desc')

        ad=Ads(img=img,desc=desc)
        ad.save()

        return redirect(reverse('blog:index'))























