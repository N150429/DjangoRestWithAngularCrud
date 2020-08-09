# Generated by Django 3.0.8 on 2020-08-02 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=23)),
                ('desc', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
