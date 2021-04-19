from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'title': 'HOME PAGE',
    }
    return render(request, template_name='blogs/home.html', context=context)

def about(request):
    return render(request, template_name='blogs/about.html')
