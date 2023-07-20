from django.db import models

class Foods(models.Model):
    name = models.CharField(max_length=500)
    desc = models.TextField()
    img = models.ImageField(upload_to='images')

# Create your models here.
