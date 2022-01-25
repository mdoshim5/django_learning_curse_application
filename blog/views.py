from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects
    print(posts)
    return render(request, 'blog/home.html', {'posts':posts})

def create(request):
    if request.method == "POST":
        if request.FILES['image'] and request.POST['title'] and request.POST['body']:
            post = Post()
            post.image = request.FILES['image']
            post.title = request.POST['title']
            post.body = request.POST['body']
            print(request)
            post.save()
            return redirect('blog')
    else:
        return render(request, 'blog/create.html')

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
    