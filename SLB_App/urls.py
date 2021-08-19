from django.conf.urls import url 
from SLB_App import views 
 
urlpatterns = [ 
    url(r'^api/home$', views.home),
   # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
   # url(r'^api/tutorials/published$', views.tutorial_list_published)
]