from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def contactUs(request):
    return render(request,'contactus.html')


def products(request):
    context = {'name':'Apple','price':100}
    #return render(request,'product/product.html',{'products':"Apple"})
    return render(request,'product/product.html',{'products':context})

def productList(request):
    
    #select * from product
    #select name, from product
    #product = Product.objects.all().values("name","price")
    product = Product.objects.filter(name="Iphone 14").values("name","price")
    product = Product.objects.filter(name= "Iphone 14",price=120000.0).values("name","price")
    product = Product.objects.get(id=1)
    
    #startswith endswith
    product = Product.objects.filter(name__istartswith="i").values("name","price")
    
    product = Product.objects.filter(name__icontains="N").values("name","price")
    
    product = Product.objects.filter(price__gt=100000.0).values("name","price")
    product = Product.objects.filter(price__gte=100000.0).values("name","price")
    #product = Product.objects.filter(price__lt=100000.0).values("name","price")
    #product = Product.objects.filter(price__lte=100000.0).values("name","price")
    product  = Product.objects.filter(name__in=["Iphone 14","Iphone 15"]).values("name","price")
    product = Product.objects.filter(price__range=(10000.0,20000.0)).values("name","price")
    product = Product.objects.filter(name__startswith="I")or Product.objects.filter(price__gt=100000.0)
    # product Product.objects.filter().
    
    print(product)
    return render(request,'product/productList.html')

def addProduct(request):
    product = Product(name = "AI",price=0.0,qty=0)
    product.save()
    print("product saved")
    return HttpResponse("Add Product")

def deleteProduct(request):
    # product = Product.objects.get(id=1)
    # deletedProduct = product.delete()
    # print(deletedProduct)
    
    products = Product.objects.filter(qty=1)
    deletedProduct = products.delete()
    print(deletedProduct)
    
    return HttpResponse("Delete Product")

def updateProduct(request,id):
    print(id)
    product = Product.objects.get(id=2)
    product.name = "Iphone 14 pro max 256 gb"
    product.price = 120000.0
    product.qty = 1
    product.save()
    print("product updated")
    return HttpResponse("Update Product")