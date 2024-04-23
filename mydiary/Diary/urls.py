from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    # TODO: Make sure that the URL paths below point to the correct corresponding views
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="diary/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("register/", views.register_view, name="register"),
]
