from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Article.models import Product,OrderDetails,OrderItems,CartItem
# Create your views here.
def payment(request):
    if request.method == "POST":
        item = CartItem.objects.filter(customer_id = request.user)
        total = 0
        for item in item:
            total = total + Product.objects.get(id = item.product_id).price
            
            
        order = OrderDetails(customer_id = request.user, total = total)
        order.save()

        
        
        CartItem.objects.filter(customer_id = request.user).delete()
        
            
        return render(request ,"payment/paymentdone.html")

        
        


    
    username = request.user.username
    user = User.objects.get(username = username)
    email = user.email
    firstname = user.first_name
    lastname = user.last_name

    return render(request ,"payment/payment.html",{ 'email' : email,
        'firstname' : firstname,
        'lastname' : lastname,
        'username' : username })

