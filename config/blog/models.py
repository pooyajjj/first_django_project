from email.policy import default
from pyexpat import model
from turtle import position
from unicodedata import category
from django.db import models
from django.utils import timezone

# Create your models here.
#fucking_github
class Category(models.Model):
    STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published')
    )
    title = models.CharField(max_length = 200, verbose_name = 'category name')
    slug = models.SlugField(max_length = 100, unique = True, verbose_name = 'category addres')
    status = models.BooleanField(default = True , verbose_name = 'show')
    position = models.IntegerField(verbose_name = 'position')
    fav = models.BooleanField(default = False)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categorys'
        ordering = ['position']

    def __str__(self):
        return self.title



class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published')
        )
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 100, unique = True)
    category = models.ManyToManyField(Category , verbose_name = 'category' )
    description = models.TextField()
    thumbnail = models.ImageField(upload_to = 'images')
    fav = models.BooleanField(default = False)
    publish = models.DateField(default = timezone.now)
    created = models.DateField(auto_now_add = True)
    created = models.DateField(auto_now = True)
    status = models.CharField(max_length = 1, choices = STATUS_CHOICES)


def __str__(self):
    return self.title