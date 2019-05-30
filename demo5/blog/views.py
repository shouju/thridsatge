from django.shortcuts import render,get_object_or_404,redirect,reverse,HttpResponse
from . models import Categories,Tag,Dynamic
from django.core.paginator import Paginator
from django.views.generic import View
from django.core.mail import send_mail,send_mass_mail
from django.core.mail import settings
# Create your views here.

def index(request):
    pagenum=request.GET.get('page')
    if pagenum==None:
        pagenum=1
    else:
        pagenum=pagenum
    dynamics=Dynamic.objects.all().order_by('-views')
    paginator=Paginator(dynamics,9)
    page=paginator.get_page(pagenum)

    return render(request,'blog/index.html',{'page':page})

def indexone(request):
    pagenum = request.GET.get('page')
    if pagenum == None:
        pagenum = 1
    else:
        pagenum = pagenum
    dynamics=Dynamic.objects.all().order_by('-views')
    paginator = Paginator(dynamics, 9)
    page = paginator.get_page(pagenum)
    return render(request, 'blog/homepage-2.html',{'page':page})

def detail(request,id):
    dynamic=get_object_or_404(Dynamic,pk=id)
    return render(request,'blog/blog-single.html',locals())

def about(request):
    return render(request,'blog/about.html')

class Contact(View):
    def get(self,request):
        return render(request, 'blog/contact.html',locals())
    def post(self,request):
        send_mail("测试邮件", "dashduahduasdjaisdhauihd", settings.DEFAULT_FROM_EMAIL, ['1120648012@qq.com', "275445831@qq.com"])
        msg=''
        return render(request,'blog/contact.html',{'msg':'发送成功'})


def categories(request,id):

    pagenum = request.GET.get('page')
    if pagenum == None:
        pagenum = 1
    else:
        pagenum = pagenum
    # return HttpResponse('success')
    dynamics= get_object_or_404(Categories, pk=id).dynamic_set.all()

    paginator = Paginator(dynamics, 6)
    page = paginator.get_page(pagenum)
    return render(request, 'blog/homepage-2.html', {'page': page})


def tags(request, id):
    pagenum = request.GET.get('page')
    if pagenum == None:
        pagenum = 1
    else:
        pagenum = pagenum
    dynamics = get_object_or_404(Tag, pk=id).dynamic_set.all()
    paginator = Paginator(dynamics, 6)
    page = paginator.get_page(pagenum)
    return render(request, 'blog/homepage-2.html', {'page': page})









