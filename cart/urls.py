from django.urls import path
from .import views

app_name = 'cart'
urlpatterns=[
    path('cart/', views.add_summary, name='add_summary'),
    path('add/', views.cart_add,name="cart_add"),
    path('delete/', views.cart_delete,name="cart_delete"),
    path('update/', views.cart_update,name="cart_update"),
      
]