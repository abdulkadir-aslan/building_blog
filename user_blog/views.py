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
                return redirect('home')
            else:
                messages.add_message(request,messages.WARNING,'Tekrar Giris Yapiniz')
    return render(request,'user_blog/login.html',{})

def user_logout(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'Oturumu Kapattiniz')
    return redirect('home')


def sign_up(request):
    if request.method == 'POST':
        r_post = request.POST
        username=r_post.get('email')
        password = r_post.get('password')
        password2 = r_post.get('password2')
        if username and (password==password2):
            user = User.objects.create_user(username,username,password)
            auth = authenticate(request,username=username,password=password)
            login(request,auth)
            messages.add_message(request,messages.SUCCESS,f'{ auth } Giris Basarili')
            return redirect('home')
        else:
            messages.add_message(request,messages.WARNING,f'Parola Hatali')
    return render(request,'user_blog/signup.html')
