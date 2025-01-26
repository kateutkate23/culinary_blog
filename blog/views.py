from django.db.models import Count
from django.shortcuts import render
from .models import Category, Post


def index(request):
    """Главная страница сайта"""
    posts = Post.objects.all()
    categories = Category.objects.annotate(post_count=Count('posts')).filter(post_count__gt=0)

    context = {
        'title': 'Главная страница',
        'posts': posts,
        'categories': categories,
    }

    return render(request, 'blog/index.html', context)


def category_list(request, pk):
    """Выбор блюд отдельной категории"""
    posts = Post.objects.filter(category_id=pk)
    categories = Category.objects.annotate(post_count=Count('posts')).filter(post_count__gt=0)

    context = {
        'title': posts[0].category,
        'posts': posts,
        'categories': categories,
    }

    return render(request, 'blog/index.html', context)