from django.shortcuts import render
from SLB_App.models import Recipe
# Create your views here.


def slb_index(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'slbIndex.html', context)


def slb_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {'recipe': recipe}
    return render(request, 'slbDetail.html', context)
