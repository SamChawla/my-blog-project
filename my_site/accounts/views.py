from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    # if request.method == 'GET':
    # import pdb;pdb.set_trace()
    form = UserCreationForm(request.GET)
    if form.is_valid():
        form.save()
        return redirect('blog-home')
    form = UserCreationForm()
    context = {
        'form': form,
        'title': 'Register User',
    }
    return render(request, 'accounts/register.html', context=context)
