from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns=[
    path('',login_page,name="login_page"),
    path('sighup_page',signup_page,name="Register_user"),
    path('welcome',welcome_page,name="welcome_page"),
    path('products',product_page,name="product_page"),
    path('cart',cart_page,name="cart_page"),
    path('details',user_details,name="user_details_page"),
    path('admin/',admin_sample,name="admin")

]
