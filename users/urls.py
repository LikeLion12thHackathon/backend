from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.Register.as_view()),
    path("users", views.PersonalProfile.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    path("signin", views.LogIn.as_view()),
    path("signout", views.LogOut.as_view()),
    path("token/refresh", views.TokenRefreshAPIView.as_view()),
]
