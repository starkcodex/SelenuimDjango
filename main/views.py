from django.shortcuts import render
from .models import Blog, BlogComment

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
    return render(request, "main/contact_us.html")


def new_emp(request):
    return render(request, "main/new_temp.html")