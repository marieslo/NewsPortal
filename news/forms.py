from django import forms
from .models import Post, SubscribersCategory

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_text', 'category']

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribersCategory
        fields = ['category']