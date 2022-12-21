from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Customer(models.Model):
    customer_id = models.OneToOneField(User, on_delete = models.CASCADE)
    

class CustomerAddress(models.Model):
    customer_id = models.OneToOneField(User, on_delete = models.CASCADE)
    address_title = models.CharField(max_length = 50)
    address_line = models.TextField()
    city = models.CharField(max_length = 50) 
    postal_code = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    def __str__(self):
        return f"{self.customer_id}"

class Category(models.Model):
    categoryName = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.categoryName
    
    def get_absolute_url(self):
        return reverse('article:category_list', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    productName = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/')
    in_stock = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.productName

 






class CustomerPayment(models.Model):
    customer_id = models.OneToOneField(User, on_delete = models.CASCADE)
    payment_type = models.CharField(max_length = 50)
    provider = models.CharField(max_length = 50)
    account_no = models.CharField(max_length = 50)
    expiry = models.DateField()
    def __str__(self):
        return f"{self.customer_id}"

class PaymentDetails(models.Model):
    order_id = models.OneToOneField(to = 'Article.OrderDetails', on_delete = models.CASCADE)
    amount = models.IntegerField()
    provider = models.CharField(max_length = 50)
    

class ShoppingPhase(models.Model):
    customer_id =models.OneToOneField(User, on_delete = models.CASCADE)
    total = models.DecimalField(max_digits = 10,decimal_places = 2)

class CartItem(models.Model):
    
    phase_id =models.OneToOneField(to = 'Article.ShoppingPhase', on_delete = models.CASCADE)
    product_id = models.IntegerField()
    quantity = models.IntegerField()

class OrderDetails(models.Model):
    
    customer_id =models.OneToOneField(User, on_delete = models.CASCADE)
    total = models.DecimalField(max_digits = 10,decimal_places = 2)
    payment_id = models.IntegerField()

class OrderItems(models.Model):
    order_id = models.OneToOneField(to = 'Article.OrderDetails', on_delete = models.CASCADE)
    product_id = models.IntegerField()
    quantity = models.IntegerField()

