from django.http import HttpResponse
from .models import Post
from django.shortcuts import render

def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "post/index.html", context)