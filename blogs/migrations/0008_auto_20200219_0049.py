# Generated by Django 2.2.5 on 2020-02-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_blog_is_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author_bio',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default='hi'),
            preserve_default=False,
        ),
    ]
