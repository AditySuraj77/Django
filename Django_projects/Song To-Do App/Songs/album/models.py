from django.db import models
from datetime import datetime

class Songlist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    artists = models.TextField(max_length=1000)
    date = models.DateField(default=datetime.now)
    img = models.ImageField(upload_to='Images')
    audio = models.FileField(upload_to='Audio')

    def __str__(self):
        return self.name


