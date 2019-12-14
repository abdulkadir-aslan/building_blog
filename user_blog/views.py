from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def user_login(request):
    if request.method == "POST":
        user_name= request.POST.get('email')
        password = request.POST.get('password')
        if user_name and password:
            user = authenticate(request,username=user_name,password=password)
            print(user)
            if user is not None:
                login(request,user)
                messages.add_message(request,messages.SUCCESS,f'Hosgeldin { user_name }')
            else:
                messages.add_message(request,messages.WARNING,'Tekrar Giris Yapiniz')
    return render(request,'user_blog/login.html',{})

def user_logout(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'Oturumu Kapattiniz')
    return redirect('home')