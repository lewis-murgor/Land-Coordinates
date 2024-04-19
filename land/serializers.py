from rest_framework import serializers
from .models import Land
from djoser.serializers import TokenSerializer
from django.contrib.auth.models import User

class LandSerializer(serializers.ModelSerializer):
    owner_username = serializers.SerializerMethodField()
    class Meta:
        model = Land
        fields = '__all__'
        read_only_fields = ["area", "owner"]

    def get_owner_username(self, obj):
        return obj.owner.username if obj.owner else None

class CustomTokenSerializer(TokenSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['username'] = instance.user.username
        return data