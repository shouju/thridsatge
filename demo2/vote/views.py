from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import VoteInfo

# Create your views here.

def index(request):
    contex={'username':'zwj'}
    return render(request,"vote/index.html",contex)

def list(request):
    allvote=VoteInfo.objects.all()
    contex = {'allvote':allvote}
    return render(request, "vote/list.html", contex)

def detail(request,id):
    contex = {}
    return render(request, "vote/detail.html", contex)
