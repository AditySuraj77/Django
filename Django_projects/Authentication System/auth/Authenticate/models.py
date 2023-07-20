from django.db import models
from django.contrib.auth.models import User

class People(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,default=True)
# Create your models here.
