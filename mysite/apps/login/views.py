from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from . import templates

# Create your views here.


def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user, username, password)
        if user is not None:
            login(request, user)
            return redirect('/userPortal/')

    context = {}
    return render(request, "login/index.html", context)
