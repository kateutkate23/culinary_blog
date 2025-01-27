from django.shortcuts import render, redirect
from .models import Category, Post
from django.db.models import F
from .forms import PostAddForm


def index(request):
    """Главная страница сайта"""
    posts = Post.objects.all().order_by('-updated_time')

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


def add_post(request):
    """Добавление поста пользователем"""
    if request.method == 'POST':
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            post.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostAddForm()

    context = {
        'title': 'Добавить статью',
        'form': form
    }

    return render(request, 'blog/add_post.html', context)
