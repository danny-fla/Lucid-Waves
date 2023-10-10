from .models import Comment
from django import forms


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'slug', 'author', 'content')

#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'slug': forms.TextInput(attrs={'class': 'form-control'}),
#             'author': forms.Select(attrs={'class': 'form-control'}),
#             'content': forms.Textarea(attrs={'class': 'form-control'}),
#         }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
