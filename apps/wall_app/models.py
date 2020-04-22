from django.db import models 
from apps.login_reg.models import *
import re 
 
# create your models here 
# Field Types Link: https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types 

class Post(models.Model):
    title = models.CharField(max_length = 255)
    message = models.TextField()
    author = models.ForeignKey('login_reg.User', related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




