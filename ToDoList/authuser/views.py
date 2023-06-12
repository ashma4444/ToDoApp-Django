from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def login(req):
    if req.method == "POST":
        name = req.POST['fname']
        password = req.POST['password']

        print(name)
        print(password)

        user = authenticate(name= name, password= password)
        if user is not None:
            return render('authuser/index.html')
            
        

    return render(req, 'authuser/login.html')

def register(req):
    if req.method == "POST":
        name = req.POST['fname']
        password = req.POST['password']

        newuser = User.objects.create(name = name, password = password)

        # newuser.name = name
        # newuser.password = password

        newuser.save()

        messages.success(req, "Your account has been created")
    return render(req, 'authuser/register.html')

