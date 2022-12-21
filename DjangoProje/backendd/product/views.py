from django.shortcuts import render

# Create your views here.
def brand(request):
    return render(request,"product/brand.html")

def shoes(request):
    return render(request,"product/shoes.html")

def jewellery(request):
    return render(request,"product/jewellery.html")

def kids(request):
    return render(request,"product/kids.html")