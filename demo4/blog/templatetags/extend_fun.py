from django import template
from ..models import Article,Category,Tag
register=template.Library()

@register.filter(name="mylower")
def mylower(value):
    return value.lower()

@register.filter(name='myslice')
def myslice(value,length):
    return value[:length]

@register.simple_tag
def getcategorys():
    return Category.objects.all()