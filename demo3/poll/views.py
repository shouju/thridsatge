from django.shortcuts import render
from django.http import HttpResponse
from .models import Qucstion,Choice
# Create your views here.


def index(request):
    # return HttpResponse("inde")
    questions=Qucstion.objects.all()
    return render(request,'poll/index.html',locals())

def detail(request,id):
    question = Qucstion.objects.get(pk=id)
    if request.method=="POST":
        return HttpResponse("11")
    return render(request, 'poll/detail.html',locals())

def result(request,id):
    # return HttpResponse("result")
    question = Qucstion.objects.get(pk=id)
    return render(request, 'poll/result.html',locals())





















