from django.urls import path
from . import views

urlpatterns = [
    path("register", views.Register.as_view()),
    path("personal-profile", views.PersonalProfile.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    path("log-in", views.LogIn.as_view()),
    path("log-out", views.LogOut.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),
    path("token/refresh", views.TokenRefreshAPIView.as_view()),
]
