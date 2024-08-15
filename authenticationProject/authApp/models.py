from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):

    COUNTRY_CHOICES = [
        ('US', 'United States'),
        ('UK', 'United Kingdom'),
        ('NIG', 'Nigeria'),
        ('SA', 'South Africa'),
        ('IN', 'India'),
        ('CA', 'Canada'),
        ('GH', 'Ghana'),
        ('AU', 'Australia')
    ]

    country = models.CharField(max_length=3, choices=COUNTRY_CHOICES)
    address = models.CharField(max_length=50, blank=True)
