from django.urls import path
from . import views

urlpatterns = [
    path("", views.slb_index, name="slb_index"),
    path("<int:pk>/", views.slb_detail, name="slb_detail"),
]
