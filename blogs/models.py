from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

'''
    Class - Pascal/Camel Case - capital for each words.
    Function - snake case - all small, _ between each words.
'''


class Blog(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    slug = models.SlugField()
    is_home = models.BooleanField(default=False)
    content = RichTextUploadingField()
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



