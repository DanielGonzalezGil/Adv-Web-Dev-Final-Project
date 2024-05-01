from django.shortcuts import render
from .models import DiaryEntry


# Create your views here.


def home(request):
    diary_entries = DiaryEntry.objects.all()
    return render(request, "home.html", {"diary_entries": diary_entries})


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")
