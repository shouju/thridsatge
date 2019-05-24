from django.shortcuts import redirect,reverse


def checklogin(fun):
    def check(request,*args):
        if request.user and request.user.is_authenticated:
            return fun(request,*args)
        else:
            return redirect(reverse('vote:login'))
    return check