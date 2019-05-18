from .models import BlogPost
from django import forms
from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class BlogForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 20, 'rows': 10}
        )
    )
    image = forms.ImageField()

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
            'image'
        ]
