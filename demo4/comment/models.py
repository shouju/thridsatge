from django.db import models
from blog.models import Article
# Create your models here.

class Comment(models.Model):
    title=models.CharField(max_length=50,verbose_name="评论")
    article=models.ForeignKey(Article,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "评论"
        verbose_name_plural = verbose_name