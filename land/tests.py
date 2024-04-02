from django.test import TestCase
from .models import Land

# Create your tests here.
class LandTest(TestCase):

    def setUp(self):
        self.land = Land(name="The Eldoret Daima Towers", coordinates={"latitude":0.515849, "longitude":35.282018}, landmark="Eldoret Daima Towers")

    def test_instance(self):
        self.assertTrue(isinstance(self.land, Land))

    def test_save_land(self):
        self.land.save_land()
        land_item = Land.objects.all()
        self.assertTrue(len(land_item) > 0)

    def test_delete_land(self):
        self.land.save_land()
        self.land.delete_land()
        land_item = Land.objects.all()
        self.assertTrue(len(land_item) == 0)
