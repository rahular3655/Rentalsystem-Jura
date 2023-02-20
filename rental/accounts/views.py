from django.shortcuts import render,redirect
from accounts.models import Account
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages,auth
from django.core.paginator import Paginator
from product.views import *

# Create your views here.


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('name')
        print(email)
        password = request.POST.get('password')
        print(password)
        try:
            user = authenticate(email=email, password=password)
            print(user,"kjsdjdhfje")
            if user is not None and user.is_superuser:
                request.session['username'] = email
                login(request, user)
                return redirect(product)
            else:
                print("else1")
                return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
        except Account.DoesNotExist:
            print("else2")
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    return render(request, "login.html")



        
def signup(request):
    if request.method =='POST':
            username=request.POST['username']
            phone_number = request.POST.get('phone_number')
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                if username== "":
                    messages.error(request,"username is empty")
                    return render(request,'signup.html')
                elif len(username)<2:
                    messages.error(request,"username is too short")
                    return render(request,'signup.html')
                elif not username.isalpha():
                    messages.error(request,"username must contain alphabets")
                    return render(request,'signup.html')
                elif not username.isidentifier():
                    messages.error(request,"username must start with alphabet")
                    return render(request,'signup.html')
                elif email=="":
                    messages.error(request,"email field is empty")
                    return render(request,'signup.html')
                elif len(email)<2:
                    messages.error(request,"emailid is too short")
                elif Account.objects.filter(email=email):
                    messages.error(request,"email is already exist,try another")
                    return render(request,'signup.html')
                else:
                    user1=Account.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email,phone_number=phone_number)
                    user1.is_active = True
                    user1.save()
                    auth.login(request,user1)
                    return redirect('signin')
                    
            else:
                messages.success(request,"password does not match")
                return redirect(request,'signup.html')
    else:
        return render(request,'signup.html')


def logoutadmin(request):
    print("error1")
    if 'username' in request.session:
        request.session.flush()
        print("error")
    logout(request)
    print("error2")
    return redirect(signin) 


def dashboard(request):
    if request.user is not None:
        return render(request,'dashboard.html')
    else:
        return messages("UnAuthorized")