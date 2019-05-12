from .models import BlogPost
from django import forms


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
            'image'
        ]
