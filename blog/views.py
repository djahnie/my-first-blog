from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponseNotFound('<h1>Sorry, no such blog post here... :(</h1>')
    return render(request, 'blog/post_detail.html', {'post': post})
