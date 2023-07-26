from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    contactno = models.CharField(max_length=10)
    birthDate = models.DateField(null=True, blank=True)
    isManager = models.BooleanField(default=False)
    isDeveloper = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'user'
    
    