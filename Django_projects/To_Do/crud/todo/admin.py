from django.contrib import admin
from .models import User
class User_todo(admin.ModelAdmin):
    list_display = ('fname','lname','email')

admin.site.register(User,User_todo)
# Register your models here.
