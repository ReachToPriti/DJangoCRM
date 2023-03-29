from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForms
from .models import Record
from .forms import AddCustomerForm
def home(request):
    records = Record.objects.all()


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
        return render(request, 'home.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request,"you have been logged out successfully!!!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForms(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login 
            username= form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username= username, password=password)
            login(request, user)
            messages.success(request,"you have successfully registered a user")
            return redirect('home')
    else:
        form=SignUpForms()    
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        #look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request,"you must login to see record")
        return redirect('home')
    
def delete_customer(request,pk):
    if request.user.is_authenticated:
        #delete records
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Customer is deleted successfully")
        return redirect('home')
    else:
        messages.success(request,"you must login to delete customer")
        return redirect('home')
    
def add_customer(request):
    form= AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Customer added...")
                return redirect('home')
        return render(request, 'add_customer.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to add Customer!")
        return redirect('home')
    
def update_customer(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        form= AddCustomerForm(request.POST or None, instance=customer_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Customer data updated successfully!")
            return redirect('home')
        return render(request,'update_customer.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to add Customer!")
        return redirect('home')
