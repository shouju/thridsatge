from django.db import models

# Create your models here.
class Qucstion(models.Model):
    title=models.CharField(max_length=30,verbose_name="问题")

    class Meta():
        verbose_name = "问题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Choice(models.Model):
    title=models.CharField(max_length=30,verbose_name="选项")
    votes=models.IntegerField(default=0,verbose_name="得票")
    qucstion=models.ForeignKey(Qucstion,on_delete=models.CASCADE)

    class Meta():
        verbose_name = "选项"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
