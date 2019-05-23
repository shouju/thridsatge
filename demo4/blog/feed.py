'''
RSS通过局和工具完成网站订阅
把内容包装成符合RSS规范的XML格式

通过重写Feed类王城XML格式内容的包装
'''
from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse


class BlogFeed(Feed):
    title='shouju的博客'
    description='分享学习经验'
    link='/'


    def items(self):
        return Article.objects.all()

    def item_title(self,item):
        return item.title

    def item_description(self, item):
        return item.body[:30]

    def item_link(self, item):
        return reverse('blog:detail',args=(item.id,))

















