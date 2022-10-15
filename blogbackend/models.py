from django.db import models

# Create your models here.
#blog表
class Post(models.Model):
    post_id = models.CharField(max_length=32,unique=True)
    update_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    type = models.TextField(verbose_name="tag")
    content = models.TextField(verbose_name="内容")