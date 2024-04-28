from django.contrib import admin

# Register your models here.
from .models import *
# inorder to store data in key value pair 
class user_details_make_key_value(admin.ModelAdmin):
    list_display=('username','password','gmail')



admin.site.register(user_details)