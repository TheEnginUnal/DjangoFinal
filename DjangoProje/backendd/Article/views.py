from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def myaccount(request):
    return render(request,"myaccount.html")

def brand(request):
    return render(request,"brand.html")

def shoes(request):
    return render(request,"shoes.html")

def jewellery(request):
    return render(request,"jewellery.html")

def kids(request):
    return render(request,"kids.html")