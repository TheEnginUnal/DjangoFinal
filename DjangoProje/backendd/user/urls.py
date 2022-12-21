from django.urls import path
from user import views


urlpatterns = [
    path("login/", views.login_request, name="login"),
    path("register/",views.register_request, name= "register"),    
    path("shopcart/",views.shopcart,name = "shopcart" ),
    path("userprofile/",views.userprofile,name="userprofile")
]