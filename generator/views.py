from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

# Home view
def home(request):
    return render(request, 'generator/home.html', {'password':'fjrnj34'})

# Password view
def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('~`!@#$%^&*()-_=+,./|{}[];:\'<>?'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

# About view
def about(request):
    return render(request, 'generator/about.html')
