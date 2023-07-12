from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isActive = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'blog'
        
    def __str__(self):    
        return self.name
    
    
    
    