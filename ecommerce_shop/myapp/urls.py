from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns=[
    path('',login_page,name="login_page"),
    path('sighup_page',signup_page,name="Register_user"),
    path('welcome',welcome_page,name="welcome_page")
]
