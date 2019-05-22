from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=30,verbose_name='分类')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "分类"
        verbose_name_plural = verbose_name

class Tag(models.Model):
    title=models.CharField(max_length=30,verbose_name='标签')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "标签"
        verbose_name_plural = verbose_name

class Article(models.Model):
    title=models.CharField(max_length=30,verbose_name='标题')
    body=models.TextField(verbose_name='内容')
    create_time=models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    update_time=models.DateTimeField(auto_now=True,verbose_name='更新时间')
    views=models.PositiveIntegerField(default=0,verbose_name='浏览次数')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类')
    tags=models.ManyToManyField(Tag,verbose_name='标签')
    auther=models.ForeignKey(User,models.CASCADE,verbose_name='作者')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "文章"
        verbose_name_plural = verbose_name
