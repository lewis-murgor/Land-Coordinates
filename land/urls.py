from django.urls import path
from . import views

urlpatterns = [
    path('lands', views.LandsView.as_view()),
    path('lands/<int:pk>', views.LandView.as_view(),)
]