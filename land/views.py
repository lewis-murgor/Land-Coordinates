from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Land
from .serializers import LandSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class LandsView(generics.ListCreateAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    permission_classes = [permissions.IsAuthenticated]

class LandView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
