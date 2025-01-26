from django import template
from django.db.models import Count
from blog.models import Category

register = template.Library()

@register.simple_tag()
def get_all_categories():
    """Все уникальные категории, в которых есть хотя бы одно блюдо"""
    return Category.objects.annotate(post_count=Count('posts')).filter(post_count__gt=0)