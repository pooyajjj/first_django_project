from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
    title = models.CharField (max_length= 200)
    slug = models.SlugField (max_length=200, unique = True)
    date_of_brith = models.DateField(default = timezone.now)

class read(models.Model):
    STATUS_CHOICES = (
    ('c', 'Compleat'),
    ('h', 'Have compleat')
    )
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 100, unique = True)
    description = models.TextField()
    publish = models.DateField(default = timezone.now)
    created = models.DateField(auto_now_add = True)
    created = models.DateField(auto_now = True)
    status = models.CharField(max_length = 1, choices = STATUS_CHOICES)



def __str__(self):
    return self.title