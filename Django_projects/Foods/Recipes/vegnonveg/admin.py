from django.contrib import admin
from .models import Foods

class Item(admin.ModelAdmin):
    list_display = ('name','desc','img')

admin.site.register(Foods,Item)
# Register your models here.
