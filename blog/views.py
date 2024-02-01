#View Blog App

from django.shortcuts import render, get_object_or_404

from .models import Post

def renderPost(request):
    total_posts = Post.objects.count()
    #posts = Post.objects.order_by("-date") #no esta funcionando, solo funciona la de abajo
    posts = Post.objects.all()
    return render(request, "blog.html",{"posts":posts, "total_posts":total_posts})

def post_detail(request, post_id):
    print(post_id)    
    post = get_object_or_404(Post, pk = post_id)
    print(post_id)
    return render(request,"post_detail.html",{"post":post})