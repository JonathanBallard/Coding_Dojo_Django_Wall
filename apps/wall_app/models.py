
from django.db import models 
from apps.login_reg.models import *
import bcrypt
import re 
import datetime


# create your models here 
# Field Types Link: https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types 

class PostManager(models.Manager):
    def post_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = "Title must contain at least 3 characters"
        if len(postData['message']) < 10:
            errors['message'] = "Message must be at least 10 characters long"
        return errors
    



class Post(models.Model):
    title = models.CharField(max_length = 255)
    message = models.TextField()
    author = models.ForeignKey('login_reg.User', related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()




class CommentManager(models.Manager):
    def comment_validator(self, postData):
        errors = {}
        if len(postData['comment']) < 5:
            errors['comment'] = "Comment must be at least 5 characters long"
        return errors


class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey('login_reg.User', related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()

