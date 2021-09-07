"""SLB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from SLB_App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("SLB_App/", include("SLB_App.urls")),
    path('', views.slb_index, name='homepage'),
    path("addRecipe/", views.slb_add_recipe, name='slb_add_recipe'),
    path("get_recipe_url/", views.get_recipe_url, name='add recipe'),
]
