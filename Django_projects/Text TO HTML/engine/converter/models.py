from django.db import models
from ckeditor.fields import RichTextField

class Editor(models.Model):
    body = RichTextField(default=True,null=True)


# Create your models here.
