from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns = [
    url(r'^indexone/$',views.indexone,name='indexone'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^about/$',views.about,name='about'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^index/$',views.index,name='index'),
]
