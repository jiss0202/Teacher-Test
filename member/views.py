from django.shortcuts import render,redirect
from .models import User
from django.contrib import auth

def index_tem(request):
    return render(request,'member/index_tem.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password']  == request.POST['password_re']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password'],
                grade = request.POST['grade'])
            auth.login(request, user)
        return redirect('login')
    return render(request, 'member/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
    return render(request,'member/login.html')

def logout(request):
    auth.logout(request)
    return render(request,'member/logout.html')

