from django import forms


class RecipeUrlForm(forms.Form):
    url = forms.URLField(label='Enter url to a recipe')
