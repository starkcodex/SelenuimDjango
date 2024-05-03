from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Error')
    else:
        form = UserCreationForm()
    return render(request, "authors/register.html" ,{'form':form})


def login(request):
    return render(request, "authors/login.html")
