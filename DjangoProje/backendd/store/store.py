
from Article.models import Product
from django.contrib.auth.models import User

class Store():

    def __init__(self, request):
        self.session = request.session
        store = self.session.get('skey')
        if 'skey' not in request.session:
            store = self.session['skey'] = {}
        self.store = store


   
    
    def add(self, product, qty):

        product_id = product.id


        if product_id not in self.store:
            self.store[product_id] = {'price' : str(product.price), 'qty' : int(qty)}

        self.save()

       


        

    def __iter__(self):

        products_ids = self.store.keys()
        product = Product.objects.filter(id__in = products_ids)
        store = self.store.copy()

        for product in product:
            store[str(product.id)]['product'] = product
        for item in store.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

        

    def __len__(self):

        return sum(item['qty'] for item in self.store.values())

    def get_total_price(self):
        return sum(int(item['price']) * item['qty'] for item in self.store.values())

    def delete(self, product):
   
        product_id = str(product)
        

        if product_id in self.store:
            del self.store[product_id]
            self.save()


    def update(self, product, qty):

        product_id = str(product)

        if product_id in self.store:
            self.store[product_id]['qty'] =  qty
        
        self.save()
    

     


    def save(self):
        self.session.modified = True 




    
