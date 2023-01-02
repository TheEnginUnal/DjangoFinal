from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from .store import Store
from Article.models import Product 
from django.http import JsonResponse
from Article.models import Product, CartItem,OrderDetails,OrderItems
from django.contrib.auth.models import User
# Create your views here.
def shopcart(request):
    store = Store(request)
    return render(request,'basket/shopcart.html', {'store' : store})

def store_add(request):
    store = Store(request)
    if request.POST.get('action') == 'post' :
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id = product_id)
        store.add(product = product, qty = product_qty) 
        storeqty = store.__len__() 

        if not CartItem.objects.filter(customer_id = request.user, product_id = product_id, quantity = product_qty):
            cart = CartItem(customer_id = request.user, product_id = product_id, quantity = product_qty)
            cart.save()
        
        response = JsonResponse({'qty' : storeqty})
        return response


def store_delete(request):
    store = Store(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        store.delete(product = product_id)
        storetotal = store.get_total_price()
        storeqty = store.__len__()
        CartItem.objects.get(customer_id = request.user, product_id = product_id).delete()



        response = JsonResponse({'qty': storeqty , 'subtotal': storetotal})
        return response

def store_update(request):
    store = Store(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        print(product_id)
        print(product_qty)
        store.update(product=product_id, qty= product_qty)

        storeqty = store.__len__()
        storetotal = store.get_total_price()

        response = JsonResponse({'qty': storeqty , 'subtotal': storetotal})
        return response





        
        


        
  


        

 