from django.db import models


# Create your models here.


class Contact(models.Model):
    CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No')
    )
    article_ready = models.CharField(verbose_name="Interested to publish article?", max_length=3, choices=CHOICES,
                                     blank=False, default='yes')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
