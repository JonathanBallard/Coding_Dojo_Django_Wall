from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
 
 
 
# Create your views here. 
def index(request): 

    thisUser = User.objects.get(id = request.session['cur_user'])
    allPosts = Post.objects.all()
    allComments = Comment.objects.all()
    context = {
        "user" : thisUser,
        "all_posts" : allPosts,
        "all_comments" : allComments,
    }

    return render(request, 'wall_app/index.html', context) 

def post(request):
    errors = Post.objects.post_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
            return redirect('/wall/')
    else:
        thisUser = User.objects.get(id=request.session['cur_user'])
        newPost = Post.objects.new_post(request.POST, thisUser)
        return redirect('/wall/')



def deletePost(request, id):
    delPost = Post.objects.get(id = id)
    if delPost.author.id == request.session['cur_user']:
        delPost.delete()
    return redirect('/wall/')

def commentPost(request, id):
    errors = Comment.objects.comment_validator(request.POST)
    if len(errors) > 0:
        for k,v in errors.items():
            messages.error(request, v)
            return redirect('/wall/')
    else:
        thisUser = User.objects.get(id = request.session['cur_user'])
        thisPost = Post.objects.get(id=id)
        Comment.objects.new_comment(request.POST, thisUser, thisPost)
        return redirect('/wall/')


def destroy(request):
    request.session.flush()
    return redirect('/')