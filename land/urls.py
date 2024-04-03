from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('lands', views.LandsView.as_view()),
    path('lands/<int:pk>', views.LandView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]