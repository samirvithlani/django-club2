from django.contrib import admin
from django.urls import path
from . import views

#admin app --> buitlin
urlpatterns = [
    path('',views.index),
    path('contactus/',views.contactUs,name='contactus'),
    path('products/',views.products,name='products'),
    path('productlist/',views.productList,name='productList'),
    path('addproduct/',views.addProduct,name='addProduct'),
    path('deleteproduct/',views.deleteProduct,name='deleteProduct'),
    #path('updateproduct/',views.updateProduct,name='updateProduct'),
    path('updateproduct/<int:id>',views.updateProduct,name='updateProduct'),
]