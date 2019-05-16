from django.db import models


# Create your models here.

class Bookinfo(models.Model):

    title=models.CharField(max_length=30,verbose_name="标题")
    pub_date=models.DateField(verbose_name="日期")

    def __str__(self):
        return self.title

GEBDLE=(("man","男"),("woman","女"))
class Heroinfo(models.Model):

    name=models.CharField(max_length=30,verbose_name="角色")
    gendle=models.CharField(max_length=10,choices=GEBDLE,verbose_name="性别")
    skill=models.CharField(max_length=30,null=True,verbose_name="技能")
    book=models.ForeignKey(Bookinfo,on_delete=models.CASCADE,verbose_name="书名")

    def __str__(self):
        return self.name