from django.shortcuts import get_object_or_404, render
from SLB_App.models import Recipe, Basket
from django.http import HttpResponseRedirect
from .forms import RecipeUrlForm, RecipeForm
from .urlScraper import scrapeUrl
from django.contrib import messages
import json
import re


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
   # basketIngs = Basket.objects.get(request).conents

    currentRecipes = basket.recipes
    if recipe.title not in currentRecipes:
        basket.contents[pk] = recipe.ingredients
        basket.recipes[pk] = recipe.title
        basket.save()
        recipe.inCart = True
        recipe.save()
        messages.success(request, "Basket Updated!")
    else:
        messages.MessageFailure(request, "Basket not updated, duplicate item")
    return slb_index(request)


def remove_from_basket(request, pk):
    print("RMB")
    recipe = get_object_or_404(Recipe, pk=pk)
    basket, created = Basket.objects.get_or_create(request)
    print(basket.recipes)
    if str(pk) in basket.recipes:
        # if recipe in currentRecipes:
        print("IN")
        recipe.inCart = False
        recipe.save()

        basket.contents.pop(str(pk))
        basket.recipes.pop(str(pk))
        basket.save()
        messages.success(request, "Basket Updated!")
    else:
        messages.MessageFailure(request, "Item not in basket. Can't remove.")
    return slb_index(request)


def view_basket(request):
    basket, created = Basket.objects.get_or_create(request)

    basketContents = sorted(list(basket.contents.values()))
    basketRecipes = list(basket.recipes.values())
    if basketRecipes == []:
        context = {"Ingredients": "No ingredients selected!",
                   "RecipeTitles": "Select a recipe "}
        return render(request, 'slbViewBasket.html', context)

    # print(basketRecipes)
    basketIngs = basketContents[0]
    for i in range(1, len(basketContents)):
        currIng = str((basketContents[i]))
       # print(currIng)
        splitPoint = currIng.index(" ")
        # print(currIng[:splitPoint])
        basketIngs += basketContents[i]
    ingredientsFormatted = []

    for i in basketIngs:
       # print("basket ings: ", i)
        units = ""
        splitPoint = i.index(" ")
        # print(i[:splitPoint], i[splitPoint:])
        ing = i[splitPoint:].lower().strip()
        qty = i[:splitPoint]
       # print(ing, "ing", qty, "qty")
        if ing.endswith("s"):
            # print(ing)
            ing = ing[:len(ing)-1]

        if ing.startswith("tsp "):
            #print("started with:", ing)
            ing = ing[3:]
            units = "tsp"
            # print(qty)
            # print(ing)
            #print("done here")
        # ingredientsFormatted.append(list([i[:splitPoint], i[splitPoint:]]))
        ingredientsFormatted.append(list([qty, ing, units]))

    # print(ingredientsFormatted)
    ingredientsFormatted = sorted(ingredientsFormatted, key=lambda x: x[1])
    ingredientsDict = {}
    for i in ingredientsFormatted:
        print("ing for", str([i[0]]), "ing: ", str([i[1]]))
        countString = (re.search(r'\d+', str([i[0]])))
        unitString = ("".join(re.findall("[a-zA-Z]", str([i[0]]))))
        if countString != None:
            countString = float(countString[0])
        else:
            countString = ""
        if unitString != None:

            unitString = str(unitString)
        if unitString == "":
            unitString = ([i[2]])[0]
        print("unit s:", unitString)
        searched = search(ingredientsDict, i[1])

        if i[1] in ingredientsDict:
            count = ingredientsDict[i[1]][0]
            count += countString

            ingredientsDict[i[1]] = [count, unitString]
           # print("here: ", i[1])

        elif searched != "":
            print("searched", searched)
            count = ingredientsDict[i[1]][0]
            count += countString

            ingredientsDict[searched] = [count, unitString]
           # ingredientsDict[searched] += countString

        else:
            ingredientsDict[i[1]] = [countString, unitString]

    # print(ingredientsDict)
    ing_out = {}
    for key in ingredientsDict:
        l = ingredientsDict[key]
        l = [str(x) for x in l]
        ing_out[key] = "".join(l)
    print("\n")
    print(ing_out)
    context = {"Ingredients": ing_out,
               "RecipeTitles": basketRecipes}
    return render(request, 'slbViewBasket.html', context)


def search(dict, searchFor):
    searchFor = searchFor.lower()
    for i in dict.keys():
       # print(i)

        if searchFor in i.lower():
            print("found: ", searchFor + " ", i)
            return i
    return ""
