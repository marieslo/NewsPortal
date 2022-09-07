import django_filters
from .models import Post, PostCategory

class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'post_title': ['icontains'],
            'post_text': ['icontains'],
            'post_time':['gte']
        }

class PostCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = PostCategory
        fields = ['category']