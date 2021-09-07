from django.db import models
from django import forms

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    steps = models.TextField()
    ingredients = models.JSONField()
    url = forms.URLField()
