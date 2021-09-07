from django.contrib import admin
from SLB_App.models import Recipe
# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
