from django.db import models

# Create your models here.

class todolist(models.Model):
    title = models.CharField(max_length = 300)
    description = models.TextField()
    is_completed = models.BooleanField()
    
    
    
    #def __str__(self):
       # return f'Title- {self.title}'
     
    
    
    