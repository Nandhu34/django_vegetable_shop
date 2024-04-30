from django.db import models

# Create your models here.
class user_details_model(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    def __str__(self):
        return f"username: '{self.username}', email: '{self.email},mobile_number:{self.mobile_number},password:{self.password}'"
    


class admin_model(models.Model):
    admin_name = models.CharField(max_length=20)
    password=  models.CharField(max_length=20)