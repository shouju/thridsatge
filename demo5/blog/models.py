from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    title=models.CharField(max_length=20,verbose_name='分类')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "分类"
        verbose_name_plural = verbose_name

class Tag(models.Model):
    title = models.CharField(max_length=20,verbose_name='标签')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "标签"
        verbose_name_plural = verbose_name

class Dynamic(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')
    body = models.TextField(verbose_name='内容')
    img=models.ImageField(upload_to='DynamicPicture',verbose_name='动态配图')
    views = models.PositiveIntegerField(default=0,verbose_name='阅读数')
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE,verbose_name='分类')
    tag=models.ManyToManyField(Tag,verbose_name='标签')
    release_time=models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "文章"
        verbose_name_plural = verbose_name