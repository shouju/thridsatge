from django.shortcuts import render,get_object_or_404,redirect,reverse
from . models import Categories,Tag,Dynamic
# Create your views here.

def index(request):
    return render(request,'index.html')

def detail(request,id):
    return render(request,'blog-single.html')



