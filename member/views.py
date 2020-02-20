from django.shortcuts import render

def signup(request):
    return render(request, 'member/signup.html')

def login(request):
    return render(request,'member/login.html')

def logout(request):
    return render(request,'member/logout.html')

