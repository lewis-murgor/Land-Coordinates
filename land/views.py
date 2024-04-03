from django.shortcuts import render
from rest_framework import generics
from .models import Land
from .serializers import LandSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class LandsView(generics.ListCreateAPIView):
    serializer_class = LandSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Land.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LandView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LandSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Land.objects.filter(owner=self.request.user)
