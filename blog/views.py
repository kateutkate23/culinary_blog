from django.shortcuts import render
from .models import Category, Post
from django.db.models import F


def index(request):
    """Главная страница сайта"""
    posts = Post.objects.all()

    context = {
        'title': 'Главная страница',
        'posts': posts,
    }

    return render(request, 'blog/index.html', context)


def category_list(request, pk):
    """Выбор блюд отдельной категории"""
    posts = Post.objects.filter(category_id=pk)

    context = {
        'title': posts[0].category,
        'posts': posts,
    }

    return render(request, 'blog/index.html', context)


def post_detail(request, pk):
    """Подробности поста"""
    Post.objects.filter(pk=pk).update(watched=F('watched') + 1)
    post = Post.objects.get(pk=pk)
    recommended_posts = Post.objects.exclude(pk=pk).order_by('-watched')[:3]

    context = {
        'title': post.title,
        'post': post,
        'recommended_posts': recommended_posts,
    }

    return render(request, 'blog/post_detail.html', context)