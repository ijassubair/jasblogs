from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

'''
    Class - Pascal/Camel Case - capital for each words.
    Function - snake case - all small, _ between each words.
'''


class Category(models.Model):
    title = models.CharField(max_length=70, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    slug = models.SlugField()
    description = models.TextField()
    is_home = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = RichTextUploadingField()
    tags = models.ManyToManyField(Tag)
    author = models.CharField(max_length=50)
    author_bio = models.TextField()
    author_photo = models.ImageField(blank=True, upload_to='author-photos/')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

