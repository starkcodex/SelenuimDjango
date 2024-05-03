from django.shortcuts import render, redirect
from .forms import SignupForm, LoginUserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is created successfully!')
            new_user = authenticate(
                username = form.cleaned_data('username'),
                password = form.cleaned_data('password1')   
            )
            
            login(request, new_user)
            return redirect('home')
        else:
            messages.error(request, 'Error')
    else:
        form = SignupForm()
    return render(request, "authors/register.html" ,{'form':form})


def login(request):
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(
                    request, f"You are logged in as {username}")
                return redirect('home')
            else:
                messages.error(request, "Error")
        else:
            messages.error(request, "Username or password incorrect")
    form = LoginUserForm()
    return render(request, "authors/login.html", {"form": form})


def logOut(request):
    logout(request)
    messages.success(request, 'You can Logged Out Successfully !')
    return redirect("home")
