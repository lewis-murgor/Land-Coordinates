from django.db import models
from django.contrib.auth.models import User
import pyproj

# Create your models here.
class Land(models.Model):
    name = models.CharField(max_length=255)
    coordinates = models.JSONField()
    landmark = models.CharField(max_length=255, default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    area = models.DecimalField(max_digits=20, decimal_places=2, default=None)

    def __str__(self):
        return self.name
    
    def extract_coordinate_list(self):
        if isinstance(self.coordinates, list):
            return [(point['latitude'], point['longitude']) for point in self.coordinates]
        else:
            return [(point['latitude'], point['longitude']) for point in self.coordinates.values()]
    
    def transform_coordinates(self, coordinate_list):
        src_crs = 'EPSG:4326'
        dst_crs = 'EPSG:3857'
        transformer = pyproj.Transformer.from_crs(src_crs, dst_crs, always_xy=True)
        return [transformer.transform(lon, lat) for lat, lon in coordinate_list]
    
    def calculate_area(self, coordinates):
        area = 0
        for i in range(len(coordinates) - 1):
            area += coordinates[i][0] * coordinates[i+1][1]
            area -= coordinates[i+1][0] * coordinates[i][1]
        area = abs(area) / 2
        area /= 10000
        return area
    
    def save(self, *args, **kwargs):
        if self.coordinates:
            coordinate_list = self.extract_coordinate_list()
            transformed_coordinates = self.transform_coordinates(coordinate_list)
            self.area = self.calculate_area(transformed_coordinates)
        super().save(*args, **kwargs)
    
    def save_land(self):
        self.save()

    def delete_land(self):
        self.delete()

