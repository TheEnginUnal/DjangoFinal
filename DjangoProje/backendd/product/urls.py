from django.urls import path
from product import views


urlpatterns = [
path("brand/",views.brand, name = "brand"),
path("jewellery/",views.jewellery , name="jewellery"),
path("kids/",views.kids, name="kids"),
path("shoes/",views.shoes, name = "shoes"),




]