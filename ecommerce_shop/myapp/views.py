from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login
# Create your views here
from pymongo import MongoClient



conn=MongoClient('mongodb://localhost:27017')
db=conn['ecommerce_shop']
coll=db['myapp_user_details_model']
def login_page(request):
    if request.method=='POST':
        form = login_form(request.POST)
       
        if form.is_valid():
           
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Example: Check username and password
            if check_username_password(request,username,password):
            # if username == 'admin' and password == 'password':
                # Authentication successful, redirect to success page

                 request.session['username'] = username
                 return redirect('welcome_page') 
            else:
                # Authentication failed, add a warning message
                print("printing warninfg mesage ")
                messages.warning(request, 'Invalid username or password.')
                return render(request, 'login_page.html', {'form': form})

    else:
        form= login_form()
        return render(request,'login_page.html',{'form':form})
    
def check_username_password(request,username,password):
    return coll.find_one({"username":username,"password":password})

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
        else:
            email_check = user_details_model.objects.filter(email=email).count()
            # count_email = coll.count_documents({"email":email})
            if email_check:
                messages.error(request, "Email already exists")
                return render(request, 'register_page.html', {'form': register_form})
            user_count = user_details_model.objects.filter(email=email).count()
            # count_mobile= coll.count_documents({"mobile_number":mobile_number})
            mobile_number_check =user_details_model.objects.filter(mobile_number=mobile_number).count()
            if mobile_number_check:
                messages.error(request, "Mobile number already exists")
                return render(request, 'register_page.html', {'form': register_form})
            

            request.session['username'] = username
            obj_user_details= user_details_model(username=username,email=email,mobile_number=mobile_number,password=password)
            obj_user_details.save()     
            print(obj_user_details.id)
            return redirect('welcome_page') 
    else:
       
        return render(request , 'register_page.html',{'form':register_form})

def get_session_data(request):
    return request.session.get('username')
def welcome_page(request):
    return render(request,'welcome.html')


def product_page(request):
    return render(request,'products.html'   )

def cart_page(request):
    print("cart page ")
    return render(request,"cart.html")

def user_details(request):
    print("user detaisl ")
    return render(request,"user_details.html")



def admin_sample(request):
    print(" admin demo ")
    return render(request, 'admin.html')