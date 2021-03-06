from django.db import models
from django import forms
from django.forms import ModelForm
# Create your models here.


class Recipe(models.Model):
    image = models.FilePathField(path="/")
    title = models.CharField(max_length=100)
    ingredients = models.JSONField()
    url = models.URLField(default="")
    inCart = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Basket(models.Model):

    contents = models.JSONField(default=dict)
    recipes = models.JSONField(default=dict)
