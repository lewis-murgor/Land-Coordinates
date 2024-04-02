from django.urls import path
from . import views

urlpatterns = [
    path('lands', views.LandsView.as_view()),
]