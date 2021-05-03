from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()
    context = {
        "form": form,
        "title": "Register User",
    }
    return render(request, "accounts/register.html", context=context)


@login_required
def profile(request):
    context = {"profile": "Sumit S Chawla", "title": "User Profile"}
    return render(request, "accounts/profile.html", context)
