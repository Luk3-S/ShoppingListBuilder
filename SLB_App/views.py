from django.shortcuts import render
from SLB_App.models import Recipe
from django.http import HttpResponseRedirect
from .forms import RecipeUrlForm
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


# def get_recipe_url(request):
#     if request.method == 'POST':
#         form = RecipeUrlForm(request.POST)
#         # if form.is_valid():
#         if (True):
#             #url = form.cleaned_data['recipe_url']
#             recipe = form.save(commit=False)
#             recipe.url = request.url
#             recipe.save()
#             # scrapeUrl(url)
#             return HttpResponseRedirect('/')
#     else:
#         form = RecipeUrlForm()
#     return render(request, 'slbAddRecipe.html', {'form': form})

def get_recipe_url(request):
    import datetime
    f = open("saveLog.txt", "a")
    f.write("in method: " + str(datetime.datetime.now()))
    if request.method == 'POST':
        f.write("before form")
        form = RecipeUrlForm(request.POST)
        f.write("got form")
        if form.is_valid():
            f.write("form valid")
            recipe = Recipe()
            recipe.url = form.cleaned_data['recipe_url']
            recipe.title = "test title"
            recipe.ingredients = "test ing"
            recipe.steps = "test ste"
            recipe.save()
            f.write("form saved?")
        f.write("form not valid")
        f.close()
    return HttpResponseRedirect('/')
