from django.contrib import admin

from .models import ToDo

class crud(admin.ModelAdmin):
    list_display = ('fname','lname','email','phone')

admin.site.register(ToDo,crud)

# Register your models here.
