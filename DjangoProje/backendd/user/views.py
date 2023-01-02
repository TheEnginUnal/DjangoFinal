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
            return redirect("home")
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
        
        


        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "user/register.html",{
                    "error" : "Kullanıcı Adı  zaten kullanılıyor",
                    "username" : username,
                    "email": email,
                    "firstname" : firstname,
                    "lastname" : lastname
                    
                    
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "user/register.html",{
                    "error" : "Email  zaten kullanılıyor",
                    "username" : username,
                    "email": email,
                    "firstname" : firstname,
                    "lastname" : lastname
                   

                })
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,
                    password = password)
                    user.save()
                    return redirect("user:login")
        else:
            return render(request,"user/register.html",{
                "error" : "Parolalar eşleşmiyor",
                "username" : username,
                    "email": email,
                    "firstname" : firstname,
                    "lastname" : lastname
                    
            })






    return render(request,'user/register.html')

    


def userprofile(request):
    if request.method == "POST":
        

        username = request.user.username
        user = User.objects.get(username = username)

        adressexits = CustomerAddress.objects.filter(customer_id = user)
        if not adressexits:
            address = CustomerAddress.objects.filter(customer_id = user)
            email = user.email
            firstname = user.first_name
            lastname = user.last_name
            address_title = request.POST["address_title"]
            address_line = request.POST["address_line"]
            city = request.POST["city"]
            postal_code = request.POST["postalCode"]
            country = request.POST["country"]
            addres = CustomerAddress(customer_id = user, address_title = address_title, address_line = address_line,
            city = city, postal_code = postal_code ,country = country)
            addres.save()
            return render(request,"user/userprofile.html", {
                'email' : email,
                'firstname' : firstname,
                'lastname' : lastname,
                'username' : username,
                'address_title' : address_title,
                'address_line' : address_title,
                'city' : city,
                'postal_code'  :postal_code,
                'country' : country

             })
        else: 
            addresdel = CustomerAddress.objects.get(customer_id = user)
            addresdel.delete()
            email = user.email
            firstname = user.first_name
            lastname = user.last_name
            address_title = request.POST["address_title"]
            address_line = request.POST["address_line"]
            city = request.POST["city"]
            postal_code = request.POST["postalCode"]
            country = request.POST["country"]
            addres = CustomerAddress(customer_id = user, address_title = address_title, address_line = address_line,
            city = city, postal_code = postal_code ,country = country)
            addres.save()
            return render(request,"user/userprofile.html", {
            'email' : email,
            'firstname' : firstname,
            'lastname' : lastname,
            'username' : username,
            'address_title' : address_title,
            'address_line' : address_title,
            'city' : city,
            'postal_code'  :postal_code,
            'country' : country

                })


       
    username = request.user.username
    user = User.objects.get(username = username)
    email = user.email
    firstname = user.first_name
    lastname = user.last_name
    address = CustomerAddress.objects.filter(customer_id = user)
    if not address:
        return render(request,"user/userprofile.html", {
        'email' : email,
        'firstname' : firstname,
        'lastname' : lastname,
        'username' : username })
    else : 
        address = CustomerAddress.objects.get(customer_id = user)
        address_title = address.address_title
        address_line = address.address_line
        city = address.city
        postal_code = address.postal_code
        country = address.country    
        return render(request,"user/userprofile.html", {
         'email' : email,
            'firstname' : firstname,
            'lastname' : lastname,
            'username' : username,
            'address_title' : address_title,
            'address_line' : address_line,
             'city' : city,
            'postal_code'  :postal_code,
            'country' : country
        })


    



    