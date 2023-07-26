#import userCreationform
from typing import Any
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class ManagerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields  = ['username','email','first_name','last_name','password1','password2']
        model = User
        
    
    @transaction.atomic
    def save(self) :
        user = super().save(commit=False)
        user.isManager = True
        user.save()
        return user
    