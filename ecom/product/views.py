from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def contactUs(request):
    return render(request,'contactus.html')


def products(request):
    context = {'name':'Apple','price':100}
    #return render(request,'product/product.html',{'products':"Apple"})
    return render(request,'product/product.html',{'products':context})