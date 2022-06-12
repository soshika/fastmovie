from django.db import models

# Create your models here.

class Movie:
    name = models.CharField(max_length=255)
