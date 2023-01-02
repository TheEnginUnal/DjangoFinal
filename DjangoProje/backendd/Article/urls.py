from django.urls import path
from Article import views



app_name = 'article'

urlpatterns = [
 
     path('<slug:category_slug>/',views.category_list, name ='category_list'),
     path('<slug:slug>', views.product_details, name='product_details'),
]