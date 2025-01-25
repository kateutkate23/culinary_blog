from django.shortcuts import render
from .models import Category, Post


def index(request):
    """Главная страница сайта"""
    posts = Post.objects.all()
    context = {
        'title': 'Главная страница',
        'posts': posts
    }

    return render(request, 'blog/index.html', context)
