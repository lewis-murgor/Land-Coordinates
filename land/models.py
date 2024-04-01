from django.db import models

# Create your models here.
class Land(models.Model):
    name = models.CharField(max_length=255)
    coordinates = models.JSONField()

class Landmark(models.Model):
    name = models.CharField(max_length=255)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
