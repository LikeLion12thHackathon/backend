from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.QuestionDetailAPIView.as_view(), name='question-detail'),
    path("", views.QuestionAPIView.as_view(), name='questions'),
]
