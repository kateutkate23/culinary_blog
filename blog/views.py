from django.shortcuts import render, redirect
from .models import Category, Post
from django.db.models import F
from .forms import PostAddForm, LoginForm, RegistrationForm
from django.contrib.auth import login, logout


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


def user_login(request):
    """Аутентификация пользователя"""
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('index')
    else:
        form = LoginForm()

    context = {
        'title': 'Войти',
        'form': form,
    }

    return render(request, 'blog/login.html', context)


def user_logout(request):
    """Выход из аккаунта"""
    logout(request)
    return redirect('index')


def user_register(request):
    """Регистрация пользователя"""
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = RegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form,
    }

    return render(request, 'blog/register.html', context)