from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify


slug = models.SlugField(blank=True)
slug = models.SlugField(unique=True)

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

    


class Gender(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'gender'

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.name



class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0, unique=False)


    def __str__(self):  # For Python 2, use __unicode__ too
        return self.title

# Create your models here.
