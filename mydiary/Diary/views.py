from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to my diary</h1>")


# function to render registration view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(
                reverse("diary:index")
            )  # TODO: make sure that 'diary:index' is the name of the correct path to redirect the user after they register
    else:
        form = UserCreationForm()
    return render(request, "diary/register.html", {"form": form})


# function to render login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(
                    reverse("diary:index")
                )  # TODO: make sure that 'diary:index' is the name of the correct path to redirect the user after they login
    else:
        form = AuthenticationForm()
    return render(request, "diary/login.html", {"form": form})


# function to render logout view
def logout_view(request):
    logout(request)
    return redirect(
        reverse("diary:login")
    )  # TODO: make sure that 'diary:login' is the name of the path for the login view
