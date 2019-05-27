from django.conf.urls import url
from . import views


app_name="vote"

urlpatterns =[
    url(r"^login/$",views.login,name="login"),
    url(r"^logout/$",views.logout,name="logout"),
    url(r"^register/$",views.register,name="register"),
    url(r"^index/$",views.index,name="index"),
    url(r"^list/$",views.list,name="list"),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^result/(\d+)/$',views.result,name='result'),
    url(r'^suggest/$',views.suggest,name='suggest'),
    # .*?  匹配所有
    url(r'^active/(.*?)/$',views.active,name='active'),
    url(r'^verify/$',views.verify,name='verify'),
    url(r'^checkuser/$',views.checkuser,name='checkuser'),
    url(r'^change_pwd',views.change_pwd,name='change_pwd'),
]