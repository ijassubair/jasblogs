from django.shortcuts import render

# Create your views here.
from blogs.models import Blog


def home(request):
    blogs = Blog.objects.all().filter(is_home=True)[:6]
    return render(request, 'pages/pages_home.html', {'blogs': blogs})


def about(request):
    return render(request, 'pages/about.html')



