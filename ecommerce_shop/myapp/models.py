from django.db import models

# Create your models here.
class user_details(models.Model):
    username= models.CharField(max_length= 50)
    password = models.CharField(max_length= 15)
    gmail = models.CharField(max_length=20)
