from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment, GalleryImage


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'excerpt', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'excerpt': SummernoteWidget(),
            'content': SummernoteWidget(),  # Use SummernoteWidget directly
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': SummernoteWidget(),  # Use SummernoteWidget directly
        }


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ('image', 'caption')

        widgets = {
            'caption': SummernoteWidget(),  # Use SummernoteWidget directly
        }
