from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate user
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you have been logged in successfully!!!")
            return redirect('home')
        else:
            messages.error(request,"There was an error in login in, please try again!!!")
            return redirect('home')
    else:          
        return render(request, 'home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"you have been logged out successfully!!!")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html',{})
