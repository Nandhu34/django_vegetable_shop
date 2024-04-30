from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *

class BlogAdminArea(admin.AdminSite):
    site_header="admin_da_nanu"
    site_title="welcome admin"
obj_custom_admin_site= BlogAdminArea(name='custom_admin')


class admin_model_in_admin(admin.ModelAdmin):
    list_display=('admin_name','password')
admin.site.register(admin_model)

# inorder to store data in key value pair 
class user_details_make_key_value(admin.ModelAdmin):
    list_display=('username','email','mobile_number','password')



admin.site.register(user_details_model)