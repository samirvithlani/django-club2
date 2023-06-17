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
    


class Course(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'course'
    
    def __str__(self):
        return self.name
    
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    course =models.ForeignKey(Course,on_delete=models.CASCADE)        
    
    class Meta:
        db_table = 'student'
    
    def __str__(self):
        return self.name
    
        
class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    
    class Meta:
        db_table = 'customer'
        
    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=50)
    customer = models.ManyToManyField(Customer)
    
    class Meta:
        db_table = 'order'
    
    def __str__(self):
        return self.name

class Sender(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'sender'
        
    def __str__(self):
        return self.name

class Receiver(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'receiver'
        
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'type'
        
    def __str__(self):
        return self.name

class Messages(models.Model):
    msg = models.CharField(max_length=50)
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
    sender = models.ForeignKey(Sender,on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    class Meta:
        db_table = 'messages'    

    def __str__(self):
        return self.msg
        