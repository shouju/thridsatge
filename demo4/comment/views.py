from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import View
from django.http import HttpResponse
from .models import Comment
from blog.models import Article
from .forms import CommentForm
# Create your views here.


class AddComment(View):
    def post(self,request,id):
        print('======================')
        article=get_object_or_404(Article,pk=id)

        cf=CommentForm(request.POST)
        if cf.is_valid():
            title=cf.cleaned_data["name"]
            email = cf.cleaned_data['email']
            url = cf.cleaned_data['url']
            comment = cf.cleaned_data['comment']

        # title=request.POST.get('name')
        # email=request.POST.get('email')
        # url=request.POST.get('url')
        # comment=request.POST.get('comment')
            print(comment,'---------------------------')

            print("-------------")
            c=Comment()
            c.title=title
            print("-----------2222")
            c.email=email
            c.url=url
            c.content=comment
            c.article=article
            c.save()
            return redirect(reverse('blog:detail',args=(id,)))
        else:
            return HttpResponse('信息不合法')


