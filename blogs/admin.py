from django.contrib import admin

# Register your models here.
from blogs.models import Blog


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Blog, BlogAdmin)
