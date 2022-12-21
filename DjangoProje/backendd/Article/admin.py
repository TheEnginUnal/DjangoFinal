from django.contrib import admin
from .models import Customer,CustomerAddress,CustomerPayment,PaymentDetails,ShoppingPhase, CartItem,OrderDetails, OrderItems,Product,Category
# Register your models here.
admin.site.register(Customer)
admin.site.register(CustomerAddress)
admin.site.register(Product)
admin.site.register(Category)

admin.site.register(CustomerPayment)
admin.site.register(PaymentDetails)
admin.site.register(ShoppingPhase)
admin.site.register(CartItem)
admin.site.register(OrderDetails)
admin.site.register(OrderItems)
