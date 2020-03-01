import random

from django.shortcuts import render, get_object_or_404

# Create your views here.
from blogs.models import Blog, Category


def home(request):
    blogs = Blog.objects.all().order_by('-pk')
    categories = Category.objects.all()
    return render(request, 'blogs/blogs_home.html', {'blogs': blogs, 'categories': categories})


def blog(request, title):
    blog_object = get_object_or_404(Blog, slug=title)
    tags = list(set(blog_object.slug.split('-')))
    related_blogs = Blog.objects.all().filter(title__in=tags, category=blog_object.category).exclude(pk=blog_object.pk)[:3]
    blog_ids = Blog.objects.all().filter(category=blog_object.category).values_list('id', flat=True)
    random_blog_ids = random.sample(
        list(blog_ids), blog_ids.count() if blog_ids.count() < 6 else 6)
    also_read_blogs = Blog.objects.filter(id__in=random_blog_ids).exclude(pk=blog_object.pk)
    return render(request, 'blogs/blogs_detail.html',
                  {'blog': blog_object, 'related_blogs': related_blogs, 'also_read': also_read_blogs})
