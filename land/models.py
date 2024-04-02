from django.db import models

# Create your models here.
class Land(models.Model):
    name = models.CharField(max_length=255)
    coordinates = models.JSONField()
    landmark = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
    
    def save_land(self):
        self.save()

    def delete_land(self):
        self.delete()

