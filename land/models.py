from django.db import models

# Create your models here.
class Land(models.Model):
    name = models.CharField(max_length=255)
    coordinates = models.JSONField()
    landmark = models.CharField(max_length=255, null=True)

