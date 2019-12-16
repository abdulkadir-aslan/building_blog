from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm


def user_login(request):
    context = {
        'form':LoginForm()
    }
    if request.method == "POST":
        # user_name= request.POST.get('email')
        # password = request.POST.get('password')
        form = LoginForm(request.POST)
        username = form.data.get('username')
        password = form.data.get('password')
        if username and password:
            user = authenticate(request,username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                messages.add_message(request,messages.SUCCESS,f'Hosgeldin { username }')
                return redirect('home')
            else:
                messages.add_message(request,messages.WARNING,'Tekrar Giris Yapiniz')
    return render(request,'user_blog/login.html',context)

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
            # user = User.objects.create_user(username,username,password)
            user,created =User.objects.get_or_create(username=username,email=username)
            if created:
                user.set_password(password)
                user.save()

            auth = authenticate(
                request,
                username=username,
                password=password
            )
            login(request,auth)
            messages.add_message(request,messages.SUCCESS,f'{ auth } Giris Basarili')
            return redirect('home')
        else:
            messages.add_message(request,messages.WARNING,f'Parola Hatali')
    return render(request,'user_blog/signup.html')
