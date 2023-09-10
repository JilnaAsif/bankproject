from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('credentials:home')
        else:
            messages.info(request,"invalid credentials")
            return redirect('credentials:login')
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username = user_name).exists():
                messages.info(request,"username taken")
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=user_name,password=password)
                user.save()
                print("User created")
                return redirect('credentials:login')
        else:
            messages.info(request,"password not matched")
            return redirect('credentials:register')
        return redirect('login.html')
    return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
def home(request):
    return render(request,"home.html")
def submit(request,):
    if request.method == 'POST':
        messages.success(request, "successfully applied")
        return redirect('credentials:apply')
def apply(request):
    return render(request,"apply.html")