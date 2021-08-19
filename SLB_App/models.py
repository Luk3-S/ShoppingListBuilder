from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=70,blank=False,default='')
    url = models.URLField()
    steps = models.TextField()

