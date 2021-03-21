from django.shortcuts import render, redirect
from django.urls import reverse
from . import templates
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.


def index(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/userPortal')

    context = {'form' : form}
    return render(request, "signUp/index.html", context=context)
