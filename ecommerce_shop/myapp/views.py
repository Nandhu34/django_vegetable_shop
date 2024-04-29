from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from .forms import *
# Create your views here


def login_page(request):
    if request.method=='POST':
        form = login_form(request.POST)
       
        if form.is_valid():
           
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Example: Check username and password
            if username == 'admin' and password == 'password':
                # Authentication successful, redirect to success page

                return redirect(welcome_page)
            else:
                # Authentication failed, add a warning message
                print("printing warninfg mesage ")
                messages.warning(request, 'Invalid username or password.')
                return render(request, 'login_page.html', {'form': form})

    else:
        form= login_form()
        return render(request,'login_page.html',{'form':form})
    


def signup_page(request):
    register_form = RegisterForm()
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            print("password not matched ")
            messages.warning(request,"Password DoesNot Match ")
            return render(request,'register_page.html',{'form':register_form})
        return redirect(welcome_page,{'name':username})
    else:
       
        return render(request , 'register_page.html',{'form':register_form})


def welcome_page(request):
    return render(request,'welcome.html')


def product_page(request):
    print("product page ")
    return render(request,'products.html')

def cart_page(request):
    print("cart page ")
    return render(request,"cart.html")

def user_details(request):
    print("user detaisl ")
    return render(request,"user_details.html")