import django.forms as forms
from .models import Blog

class BlogCreateionForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields ='__all__'