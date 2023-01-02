from django.urls import path
from user import views



app_name = 'user'
urlpatterns = [
    path("login/", views.login_request, name="login"),
    path("register/",views.register_request, name= "register"),    
    
    path("userprofile/",views.userprofile,name="userprofile"),
    


]