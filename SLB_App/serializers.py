from rest_framework import serializers 
from SLB_App.models import Recipe
 
 
class RecipeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Recipe
        fields = ('id',
                  'title',
                  'url'
                  'steps')