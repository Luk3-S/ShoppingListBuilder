from django.shortcuts import render
from SLB_App.models import Recipe
from django.http import HttpResponseRedirect
from .forms import RecipeUrlForm, RecipeForm
from .urlScraper import scrapeUrl


def slb_index(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'slbIndex.html', context)


def slb_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {'recipe': recipe}
    return render(request, 'slbDetail.html', context)


def slb_add_recipe(request):
    return render(request, 'slbAddRecipe.html', {})


def get_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            fo = form.save(commit=False)
            title, ingredients, steps = scrapeUrl(fo.url)
            fo.ingredients = ingredients
            fo.steps = steps
            fo.title = title
            fo.save()

            return HttpResponseRedirect('.')
    else:

        form = RecipeForm()
    return render(request, 'slbAddRecipe.html', {'form': form})
