from django import template
from ..models import Dynamic,Tag,Categories
register=template.Library()

# 过滤字体   去前n个字体
@register.filter(name='myslice')
def myslice(value,length):
    return value[:length]

# 转小写
@register.filter(name='mylower')
def mylower(value):
    value.lower()

# 获取最近的文章
@register.simple_tag
def getlaterdynamics(num):
    return Dynamic.objects.all().order_by('-release_time')[:num]

# 获取分类的所有文章
@register.simple_tag
def getcategories():
    return Categories.objects.all()

# 获取标签文章
@register.simple_tag
def gettags():
    return Tag.objects.all()








