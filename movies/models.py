from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=255)
    director = models.CharField(max_length=255, verbose_name=_('Director'))
    cast = models.CharField(max_length=255, verbose_name=_('Cast'))
    generes = models.CharField(max_length=255, verbose_name=_('Generes'))
    release_year = models.CharField(max_length=8, verbose_name=_('ReleaseYear'))
    country = models.CharField(max_length=128, verbose_name=_('country'))
    description = models.TextField()
    url = models.CharField(max_length=255, verbose_name=_('URL'))
    thumbnail = models.CharField(max_length=255, verbose_name=_('Thumbnail'))


class Genres(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('Name'))


class Countries(models.Model):
    name = models.CharField(max_length=32, verbose_name=_('Name'))
    img = models.CharField(max_length=255, verbose_name=_("img"))
