from django import forms
from django.forms import ModelForm
from SLB_App.models import Recipe


class RecipeUrlForm(forms.Form):
    url = forms.URLField(label='Enter url to a recipe')


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['url']
