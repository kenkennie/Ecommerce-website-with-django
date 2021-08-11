#from django.http import  JsonResponse, request
import json
from django.http import response
from django.http.response import  JsonResponse
from django.shortcuts import get_object_or_404, render
from store.models import Product

from .cart import Cart


# Create your views here.
def add_summary(request):
    cart =Cart(request)
    print (cart)
    return render(request, 'cart/cart.html', {'cart':cart})

    # get product id when add to cart btn is clicked
def cart_add(request):
    cart = Cart(request)
    # first get session data from class Cart
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        # get product  id from the  whrn clicked

        product =  get_object_or_404(Product, id=product_id)
        # get product id from Product model
        cart.add(product = product ,qty = product_qty)
        # create class to add/save data
        baskettotalqty = cart.__len__()
        # capture total sum of qty when added to cart 

        
        response = JsonResponse({'qty':baskettotalqty,})
        return response


# Delete from session data
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action')=='delete':
        product_id = int(request.POST.get('productid'))
        cart.delete(product = product_id)
        response = JsonResponse({'success':True})
        return response


#Update cart
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action')=='update':
        product_id = int(request.POST.get('productid'))
        
        product_qty =str(request.POST.get('productqty'))

        #cart = cart.__len__()
        print(product_id)
        print(product_qty)
        response = JsonResponse({'Success':True})
        return response