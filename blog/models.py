
from django.db import models
#makemigrations - create changes and store in a file
#migrate-apply the pending changes made by makemigrations
class Subscribe(models.Model):# subscribe vanne table banaunxa with columns name,email and date
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    date=models.DateField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)  
    message=models.CharField(max_length=222)
    date=models.DateField()

    def __str__(self): 
        return self.name 

class Teacher_Sign(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40) 
    address=models.CharField(max_length=40) 
    phone=models.IntegerField(null=True)
    city=models.CharField(max_length=40)
    country=models.CharField(max_length=40)
    zip=models.IntegerField(null=True)
    #photo=models.FileField()
    degree=models.CharField(max_length=40)
    university=models.CharField(max_length=40)
    #certificate=models.CharField(max_length=40)
    subject=models.CharField(max_length=40,default="")
    experience=models.CharField(max_length=4)
    week=models.CharField(max_length=4)
    medium=models.CharField(max_length=40)
    date=models.DateField()
    def __str__(self): 
        return self.name 

class Student_Sign(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40) 
    address=models.CharField(max_length=40) 
    phone=models.IntegerField(null=True)
    city=models.CharField(max_length=40)
    country=models.CharField(max_length=40)
    zip=models.IntegerField(null=True)
    #photo=models.FileField()
    degree=models.CharField(max_length=40)
    school=models.CharField(max_length=40)
    #certificate=models.CharField(max_length=40)
    subject=models.CharField(max_length=40,default="")
    experience=models.CharField(max_length=4)
    week=models.CharField(max_length=4)
    medium=models.CharField(max_length=40)
    date=models.DateField()
    def __str__(self): 
        return self.name 