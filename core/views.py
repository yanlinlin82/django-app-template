from django.shortcuts import render, redirect
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

def home(request):
    return render(request, 'core/index.html')

def login(request):
    do_login(request, request.user)
    return redirect('home')

def logout(request):
    do_logout(request)
    return redirect('home')
