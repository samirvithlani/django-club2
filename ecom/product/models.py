from django.db import models

# Create your models here.
#product table.... id name price create table product(id int primary key auto_increment,name varchar(50),price int);
#orm

options = (('1','Active'),('0','Inactive'))

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    qty = models.IntegerField()
    status = models.BooleanField(default=True)
    color = models.CharField(max_length=50,null=True)
    choice = models.CharField(max_length=20,choices=options,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    avaialableDate = models.DateField(null=True)
    avaialbletime = models.TimeField(null=True)
    avaialbleDttime = models.DateTimeField(null=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product'
    

class Code(models.Model):
    code = models.CharField(max_length=50)
    
    def __str__(self):
        return self.code
    
    class Meta:
        db_table = 'code'

class Book(Code):
    name = models.CharField(max_length=50)        
    
    class Meta:
        db_table = 'book'
    
    def __str__(self):
        return self.name    