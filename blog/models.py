from django.db import models
from django.urls import reverse

class Category(models.Model):
    """Категория блюда"""
    title = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    """Для постов"""
    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    content = models.TextField(default='Новая статья...', verbose_name='Текст статьи')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='media/', blank=True, null=True, verbose_name='Изображения')
    watched = models.IntegerField(default=0, verbose_name='Просмотры')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'