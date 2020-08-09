from django.db import models

# Create your models here.

class Movie(models.Model):
	title = models.CharField(max_length=23)
	desc = models.CharField(max_length=200)
	year = models.IntegerField()
	