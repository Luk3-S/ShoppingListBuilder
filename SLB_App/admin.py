from django.contrib import admin
from SLB_App.models import Recipe, Basket
# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    pass


class BasketAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Basket, BasketAdmin)
