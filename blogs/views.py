from django.shortcuts import render, get_object_or_404

# Create your views here.
from blogs.models import Blog


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/blogs_home.html', {'blogs': blogs})


def blog(request, title):
    # try:
    #     blog_object = Blog.objects.get(slug=title)
    # except Blog.DoesNotExist:
    #     raise Http404
    blog_object = get_object_or_404(Blog, slug=title)
    return render(request, 'blogs/blogs_detail.html', {'blog': blog_object})

