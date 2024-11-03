from django.db import models

class Employee(models.Model):
     empcode =models.IntegerField()
     name = models.CharField(max_length=30)
     mobile =models.CharField(max_length=10)
     email =models.EmailField(max_length=50)
