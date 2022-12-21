from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from Article.models import CustomerAddress

# Create your views here.l
def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]

        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return render(request, "index.html",{"account": "deneme"})
        else: 
            return render(request, "user/login.html", {
                "error" : "Kullanıcı adı veya parolo hatalı"
                
            })
    return render(request,"user/login.html")
    

def register_request(request):
    if request.method == "POST":
        username = request.POST["userName"]
        firstname = request.POST["firstName"]
        email = request.POST["email"]
        lastname = request.POST["lastName"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        phone = request.POST["phone"]
        


        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "user/register.html",{
                    "error" : "Kullanıcı Adı  zaten kullanılıyor",
                    "username" : username,
                    "email": email,
                    "firstname" : firstname,
                    "lastname" : lastname,
                    "phone" : phone
                    
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "user/register.html",{
                    "error" : "Email  zaten kullanılıyor",
                    "username" : username,
                    "email": email,
                    "firstname" : firstname,
                    "lastname" : lastname,
                    "phone" : phone

                })
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,
                    password = password)
                    user.save()
                    return render(request,"user/login.html",{
                        "message" : "Kayıt Başarılı Lütfen Giriş Yapınız"
                    })
        else:
            return render(request,"user/register.html",{
                "error" : "Parolalar eşleşmiyor",
                "username" : username,
                    "email": email,
                    "firstname" : firstname,
                    "lastname" : lastname,
                    "phone" : phone
            })






    return render(request,'user/register.html')

    
def shopcart(request):
    return render(request,'user/shopcart.html')

def userprofile(request):
    if request.method=="POST":
        addres = CustomerAddress()
        addres.customer_id = User.objects.get(pk =1)
        addres.address_title = request.POST["address"]
        addres.address_line = "Deneme"
        addres.city = request.POST["city"]
        addres.country = request.POST["country"]
        addres.postal_code = request.POST["postalCode"]
        addres.save()
        return redirect("home")
    return render(request,"user/userprofile.html")



    