from django.http import HttpResponse
from .models import Post
from django.shortcuts import render
from .forms import PostForm

def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "post/index.html", context)

def create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базу данных
            return render(request, 'post/success.html')
    else:
        form = PostForm()
    return render(request, 'post/create.html', {'form': form})