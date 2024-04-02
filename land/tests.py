from django.test import TestCase
from .models import Land
from django.core.exceptions import ValidationError

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

    def test_invalid_land(self):
        with self.assertRaises(ValidationError):
            invalid_land = Land(name="", coordinates={"latitude": 0.515849, "longitude": 35.282018})
            invalid_land.full_clean()

    def test_update_land(self):
        self.land.save_land()
        new_name = "Different Land Name"
        self.land.name = new_name
        self.land.save_land()
        updated_land = Land.objects.get(id=self.land.id)
        self.assertEqual(updated_land.name, new_name)
