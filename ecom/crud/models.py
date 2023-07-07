from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount= models.FloatField()
    is_active = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    description = models.TextField()
    
    class Meta:
        db_table = 'product1'
    
    def __str__(self):
        return self.name
    
    