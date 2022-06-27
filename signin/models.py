from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=128, verbose_name=_('Username'))
    email = models.EmailField(max_length=255, verbose_name=_('Email'))

