"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include #include is used to include the urls of other apps
from . import views

#admin app --> buitlin
urlpatterns = [

    path('create/',views.create_ProductView,name='create_product'),
    path('list/',views.product_list,name='product_list'),
    path('delete/<int:id>/',views.delete_product,name='delete_product'),
    path('update/<int:id>/',views.update_product,name='update_product'),
]
