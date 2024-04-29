from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .models import DiaryEntry


# Create your views here.
def base(request):
    diary_entries = DiaryEntry.objects.all()
    return render(request, "home.html", {"diary_entries": diary_entries})
