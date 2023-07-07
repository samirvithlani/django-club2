
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        #fields = ['name','price','discount','is_active','is_available','description']
        fields = '__all__'
