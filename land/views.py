from django.shortcuts import render
from rest_framework import generics
from .models import Land
from .serializers import LandSerializer

# Create your views here.
class LandsView(generics.ListCreateAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
