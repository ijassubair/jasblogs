# Generated by Django 2.2.5 on 2020-01-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20200109_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]
