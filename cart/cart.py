'''
Created on 2 Sep 2019

@author: benjaminsenyonyi
'''

from decimal import Decimal
from django.conf import settings
from hep_django_project.shop.models import Product #here

class Cart(object):
    '''
    classdocs
    '''


    def __init__(self, request):
        '''
        Cart initializer
        '''
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    
    def add(self, product, quantity=1, update_quantity=False):
        '''
        Add products to cart
        '''
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
    
    
    def save(self):
        '''
        modified session saved
        '''
        self.session.modified = True

    
    def remove(self, product):
        '''
        remove product from cart
        '''
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    
    def __iter__(self):
        '''
        Iterations
        '''
        product_ids = self.cart.keys()
        products = Product.objects.filter(id_in = product_ids)
        
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
#             use yield to return the iteration of numbers
            yield item
        
    
    def get_total_price(self):
        total_price = sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
        return total_price
    
    def __len__(self):
        '''
        Count items in cart
        '''
        item_sum = sum(item['quantity'] for item in self.cart.values())
        return item_sum

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
    
    
    












      
    