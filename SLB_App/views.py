from django.shortcuts import get_object_or_404, render
from SLB_App.models import Recipe, Basket
from django.http import HttpResponseRedirect
from .forms import RecipeUrlForm, RecipeForm
from .urlScraper import scrapeUrl
from django.contrib import messages


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
            title, ingredients, image = scrapeUrl(fo.url)
            if image == "":
                image = "/static/apple.jpg"
            fo.ingredients = ingredients
            fo.image = image
            fo.title = title
            fo.save()

            return HttpResponseRedirect('.')
    else:

        form = RecipeForm()
    return render(request, 'slbAddRecipe.html', {'form': form})


def add_to_basket(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    basket, created = Basket.objects.get_or_create(request)

    currentRecipes = basket.recipes
    if recipe.title not in currentRecipes:
        basket.contents += recipe.ingredients
        basket.recipes.append(recipe.title)
        basket.save()
        messages.success(request, "Basket Updated!")
    else:
        messages.MessageFailure(request, "Basket not updated, duplicate item")
    return slb_index(request)
