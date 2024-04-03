from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Land(models.Model):
    name = models.CharField(max_length=255)
    coordinates = models.JSONField()
    landmark = models.CharField(max_length=255, default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
    
    def save_land(self):
        self.save()

    def delete_land(self):
        self.delete()

        