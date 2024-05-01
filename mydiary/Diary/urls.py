from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),  # This one works
    path("register/", views.register, name="register"),  # This one does not work
    path("login/", views.login, name="login"),  # this one does not work
]
