from asyncio.windows_events import NULL
import email
from email.headerregistry import Address
from msilib import change_sequence
from django.db import models
from django.forms import CharField

# Create your models here.
class parent(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=8)
    nationality=models.CharField(max_length=20)
    dateofbirth=models.DateField( auto_now_add=False,auto_now=False,blank=True,null=True)
    occupation=models.CharField(max_length=20)
    contact1=models.IntegerField(default=0)
    email=models.EmailField(max_length=20)
    Address=models.CharField(max_length=50)
    child_maintenance_amount=models.IntegerField(default=0)
    motivation=models.CharField(max_length=100)   
    def __str__(self):
        return self.name

class child(models.Model):
    regno=models.IntegerField(default=0)
    orgname=models.CharField(max_length=50 ,default="mother therisa org")
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=15)
    dateofbirth=models.DateField( auto_now_add=False,auto_now=False,blank=True,null=True)
    fathername=models.CharField(max_length=20)
    mothername=models.CharField(max_length=20)
    address=models.CharField(max_length=30)

    def __str__(self):
        return self.name

        

class details(models.Model):
   child =models.ForeignKey(child, on_delete=models.CASCADE)
   parent=models.ForeignKey(parent, on_delete=models.CASCADE)
   
   '''def __str__(self):
        return self.child.name + "__"+self.parent.name'''