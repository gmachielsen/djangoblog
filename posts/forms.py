from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ( 'title', 'content', 'tag', 'image', 'author', 'painting_type')
        
        
class BlogPostFilterForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('painting_type', 'medium', 'level')
        