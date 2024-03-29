from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from ..shop.models import Product #here
from .cart import Cart 
from .forms import CartAddProductForm


# Create your views here.
@require_POST

def cart_add(request, product_id):
    '''
    Add products to the cart
    '''
    cart=Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    '''
    Remove product through ID from the cart
    '''
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    '''
    Get cart details
    '''
    cart =Cart(request)
    return render(request, 'cart/detail.html', {'cart' : cart})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product':product, 'cart_product_form':cart_product_form})
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    