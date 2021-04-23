from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
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
