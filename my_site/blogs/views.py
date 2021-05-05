from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


def home(request):
    posts = Post.published.all()

    context = {
        "title": "HOME PAGE",
        "posts": posts,
    }
    return render(request, template_name="blogs/home.html", context=context)


def about(request):
    return render(request, template_name="blogs/about.html")


class PostListView(ListView):
    model = Post
    queryset = Post.published.all()
    template_name = 'blogs/home.html'
    context_object_name = 'posts'
    ordering = ['-published_at']

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     return qs.filter(status='published') 

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data()
        context_data['title'] = "BLOG HOME PAGE"
        return context_data

post_list_view = PostListView.as_view()


class PostDetailView(DetailView):
    model = Post
    # pk_url_kwarg = 'id'

post_detail_view = PostDetailView.as_view()