from django.db import models

#import models
from App_Account.models import User
# Create your models here.

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='taskauthor')
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True,max_length=1000)
    status=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return self.title
    
    
