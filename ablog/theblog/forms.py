from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')
choices_list = []

for obj in choices:
    choices_list.append(obj)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body','comment')
        widgets = {
            'name': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'image_header')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control', 'value': '', 'id': 'elder'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'title_tag', 'body', 'snippet'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }
