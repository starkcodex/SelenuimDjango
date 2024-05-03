from django.shortcuts import render, redirect
from .models import Blog, BlogComment
from .forms import ContactForm
from django.contrib import messages


def home(request):
    all_blogs = Blog.objects.all()
    context = {'all_blogs': all_blogs}
    print(all_blogs)
    return render(request, "main/blog_home.html", context)


def detail(request, slug_url):
    blog = Blog.objects.get(slug=slug_url)
    all_blogs = Blog.objects.all().order_by('-post_date')[:3]
    context = { 'blog': blog, 'all_blogs': all_blogs}
    return render(request, "main/blog_detail.html", context)


def profile(request):
    return render(request, "main/profile.html")


def contact_us(request):
    form=ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "your form is submitted successfully. ")
    else:
        form = ContactForm()
    return render(request, "main/contact_us.html", {"form":form})


def new_emp(request):
    return render(request, "main/new_temp.html")