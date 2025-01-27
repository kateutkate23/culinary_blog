from django import forms
from .models import Post


class PostAddForm(forms.ModelForm):
    """Форма для добавления новой статьи пользователем"""

    class Meta:
        """Класс, указывающий поведенческий характер"""
        model = Post
        fields = ['title', 'content', 'photo', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
