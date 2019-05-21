from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VoteInfo(models.Model):

    matter=models.CharField(max_length=20,verbose_name="投票问题")
    choose1 = models.CharField(max_length=10,verbose_name="选项1")
    choose2 = models.CharField(max_length=10,verbose_name="选项2")
    choose1vote = models.IntegerField(default=0)
    choose2vote = models.IntegerField(default=0)

    def __str__(self):
        return self.matter

class MyUser(User):
    url = models.URLField(blank=True, null=True, default="http://www.baidu.com")
    class Meta():
        verbose_name = "用户"
        verbose_name_plural = verbose_name


