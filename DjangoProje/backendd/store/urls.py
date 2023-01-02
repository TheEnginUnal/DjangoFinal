from django.urls import path
from . import views
app_name = 'store'
urlpatterns = [

   path("shopcart/",views.shopcart,name = "shopcart" ),
   path("add/", views.store_add, name='store_add'),
   path("delete/", views.store_delete, name='store_delete'),
   path("update/", views.store_update, name='store_update'),
    
    


    
]