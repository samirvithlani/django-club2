from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect

# Create your views here.

def create_ProductView(request):
    context = {}
    form = ProductForm(request.POST or None)
    context['form'] = form
    if form.is_valid():
        x = form.save()
        print(x)
        return redirect('create_product')
    
    return render(request,'crud/create_product.html',context)


def product_list(request):
    context = {}
    product = Product.objects.all().values()
    context['products'] = product
    return render(request,'crud/product_list.html',context)
    

def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product_list')


def update_product(request,id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None,instance=product)
    context = {}
    context['form'] = form
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request,'crud/create_product.html',context)
    
    
