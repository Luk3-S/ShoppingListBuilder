from django.urls import path
from . import views

urlpatterns = [
    path("", views.slb_index, name="slb_index"),
    path("<int:pk>/", views.slb_detail, name="slb_detail"),
    path("addRecipe", views.slb_add_recipe, name='slb_add_recipe'),
    path("add_to_basket/<int:pk>/", views.add_to_basket, name="add_to_basket"),
]
