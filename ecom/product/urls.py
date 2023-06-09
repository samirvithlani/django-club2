from django.contrib import admin
from django.urls import path
from . import views

#admin app --> buitlin
urlpatterns = [
    path('',views.index),
    path('contactus/',views.contactUs,name='contactus'),
    path('products/',views.products,name='products'),
]