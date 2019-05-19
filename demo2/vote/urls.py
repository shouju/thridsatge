from django.conf.urls import url
from . import views


app_name="vote"

urlpatterns =[
    url(r"^index/$",views.index,name="index"),
    url(r"^list/$",views.list,name="list"),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^result/(\d+)/$',views.result,name='result'),
]