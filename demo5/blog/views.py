from django.shortcuts import render,get_object_or_404,redirect,reverse
from . models import Categories,Tag,Dynamic
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    pagenum=request.GET.get('page')
    if pagenum==None:
        pagenum=1
    else:
        pagenum=pagenum
    dynamics=Dynamic.objects.all().order_by('-views')
    paginator=Paginator(dynamics,3)
    page=paginator.get_page(pagenum)

    return render(request,'blog/index.html',{'page':page})

def indexone(request):
    pagenum = request.GET.get('page')
    if pagenum == None:
        pagenum = 1
    else:
        pagenum = pagenum
    dynamics=Dynamic.objects.all().order_by('-views')
    paginator = Paginator(dynamics, 3)
    page = paginator.get_page(pagenum)
    return render(request, 'blog/homepage-2.html',{'page':page})

def detail(request,id):
    dynamic=get_object_or_404(Dynamic,pk=id)
    return render(request,'blog/blog-single.html',locals())

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')


