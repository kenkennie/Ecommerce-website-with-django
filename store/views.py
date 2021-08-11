from django.http import request
from django.shortcuts import get_object_or_404, render

from .models import Category, Product

# HOME PAGE
def index(request):
    products= Product.objects.all()
   
    return render(request, 'index.html',{'products':products,})
    
# SHOP PAGE
def shop(request):
    products= Product.objects.all()
   
    return render(request, 'shop.html',{'products':products,})

# PRODUCT DETAIL
def product_detail(request,slug):
   product = get_object_or_404(Product,slug=slug,in_stock=True)
   return render(request, 'product-details.html',{'product':product})






def product_category(request, product_category_slug,):
    categ = get_object_or_404(Category,slug = product_category_slug)
    products = Product.objects.filter(category=categ)
    return render (request, 'product-categories.html', {'productsCateg': products,'categ':categ })


def category(request,category_slug,):
    categ =get_object_or_404(Category,slug = category_slug)
    products = Product.objects.filter(category=categ) #filter from Product  - category model
    return render(request, 'store/products/categories.html',{'productCateg':products,'categ':categ})