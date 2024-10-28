import unittest
from app.models.amenity import Amenity
from app.services.facade import HBnBFacade

class TestAmenity(unittest.TestCase):
    """Test cases for Amenity model and API endpoints"""

    def setUp(self):
        self.facade = HBnBFacade()
        self.amenity_data = {
            "name": "Wifi"
        }

    def test_create_amenity(self):
        """Test that amenity is created with right attributes"""
        amenity = Amenity(**self.amenity_data)
        self.assertEqual(amenity.name, "Wifi")
        self.assertIsInstance(amenity.id, str)

        #amenity = Amenity(name= " Wifi ") # Check for name stripping and whitespaces
        #self.assertEqual(amenity.name, "Wifi")
        
        #with self.assertRaises(ValueError): # Check for invalid data input
            #Amenity(name="")

        #with self.assertRaises(TypeError):
            #Amenity(name=123)

        #with self.assertRaises(TypeError): # Cheack if test None name
            #Amenity(name=None)

    def test_facade_create_amenity(self):
        """Test creating amentiy through facade"""
        amenity = self.facade.create_amenity(self.amenity_data)
        self.assertEqual(amenity.name, "Wifi")
        self.assertIsInstance(amenity.id, str)

    def test_facade_get_amenity(self):
        """Test to get data through facade"""
        created = self.facade.create_amenity(self.amenity_data)

        retrieved = self.facade.get_amenity(created.id)
        self.assertEqual(retrieved.name, created.name)

        retrieved = self.facade.get_amenity_by_name("Wifi")
        self.assertEqual(retrieved.id, created.id)

    def test_facade_get_all_amenities(self):
        """Test getting all amenities through facade"""
        self.facade.create_amenity({"name": "Wifi"})
        self.facade.create_amenity({"name": "Air Conditioner"})

        amenities = self.facade.get_all_amenities()
        self.assertEqual(len(amenities), 2)
        self.assertEqual(sorted([amenity.name for amenity in amenities]),
                         ["Air Conditioner", "Wifi"])

if __name__ == '__main__':
    unittest.main()
