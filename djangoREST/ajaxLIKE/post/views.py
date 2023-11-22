from django.shortcuts import render
from .models import Post, Like
from django.http import HttpResponse 

def indexView(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def likepostView(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(pk=post_id)
        m = Like(post=likedpost)
        m.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Response method is not GET")