from django.contrib import admin
from .models import Songlist

class Audio(admin.ModelAdmin):
    list_display = ('name','genre','artists','date','img','audio')

admin.site.register(Songlist,Audio)


# Register your models here.
