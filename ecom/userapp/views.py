from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import ManagerCreationForm
from .models import User

# Create your views here.
class ManagerRegisterView(CreateView):
    form_class = ManagerCreationForm
    model = User
    template_name = 'userapp/manager_register.html'
    success_url = '/'
    
