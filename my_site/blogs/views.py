from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        "author": "Sumit S Chawla",
        "date_posted": datetime.now(),
        "title": "My First Post",
        "content": "This is a sample post",
    },
    {
        "author": "Sumit",
        "date_posted": datetime.now(),
        "title": "My Second Post",
        "content": "This is another sample post",
    }
]


def home(request):
    context = {
        'title': 'HOME PAGE',
        'posts': posts,
    }
    return render(request, template_name='blogs/home.html', context=context)

def about(request):
    return render(request, template_name='blogs/about.html')
