# Generated by Django 3.0.8 on 2020-08-09 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_movie_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='img',
        ),
    ]
