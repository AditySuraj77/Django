from django.db import models

class ToDo(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=500)
    phone = models.IntegerField()
# Create your models here.
