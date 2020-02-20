from django.shortcuts import render
from .models import User
from django.contrib import auth


def signup(request):
    if request.method == "POST":
        if request.POST['password']  == request.POST['password_re']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password'],
                grade = request.POST['grade'])
            auth.login(request, user)
        return render(request,'member/login.html')
    return render(request, 'member/signup.html')

def login(request):
    return render(request,'member/login.html')

def logout(request):
    return render(request,'member/logout.html')

