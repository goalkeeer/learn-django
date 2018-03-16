from django.conf.urls import url
from django.views.generic import ListView, DetailView
from news.models import Post
from . import views

urlpatterns = [
    url(r'^$',
        ListView.as_view(queryset=Post.objects.all().order_by('-date'),
                         template_name='news/index.html',)),
    url(r'^/(?P<pk>\d+)$',
        DetailView.as_view(model=Post, template_name='news/post.html'))
]
