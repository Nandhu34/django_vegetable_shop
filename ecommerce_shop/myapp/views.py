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

    return render(request,'register_page.html')


def welcome_page(request):
    return render(request,'welcome.html')