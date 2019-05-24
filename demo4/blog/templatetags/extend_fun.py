from django import template
from ..models import Article,Category,Tag,Ads
register=template.Library()
"""
过滤器最多两个参数
白浅可以有人以个参数

"""
@register.filter(name="mylower")
def mylower(value):
    return value.lower()

@register.filter(name='myslice')
def myslice(value,length):
    return value[:length]

@register.simple_tag
def getcategorys():
    return Category.objects.all()

@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def getarchives(num=3):
    result=Article.objects.dates('create_time','month',order='DESC')[:num]
    print(result)
    return result

@register.simple_tag
def gettags():
    return Tag.objects.all()

@register.simple_tag
def getads():
    return Ads.objects.all()










