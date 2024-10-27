import unittest
from uuid import UUID
from app.models.amenity import Amenity
from app.services.facade import HBnBFacade
from app import create_app

class TestAmenity(unittest.TestCase):
    """Test cases for Amenity model and API endpoints"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.facade = HBnBFacade()

        self.amenity_data = {
            "name": "Wifi"
        }

    def tearDown(self):
        """Cleaning up after each test"""
        if hasattr(self.facade, 'amenity_repo'):
            self.facade.amenity_repo.clear()

    def test_create_amenity(self):
        """Test that amenity is created with right attributes"""
        amenity = Amenity(**self.amenity_data)
        self.assertEqual(amenity.name, "Wifi")
        self.assertIsInstance(amenity.id, str)

        amenity = Amenity(name= " Wifi ") # Check for name stripping and whitespaces
        self.assertEqual(amenity.name, "Wifi")
        
        with self.assertRaises(ValueError): # Check for invalid data input
            Amenity(name="")

        with self.assertRaises(TypeError):
            Amenity(name=123)

        with self.assertRaises(TypeError): # Cheack if test None name
            Amenity(name=None)

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
                         ["Air Conditioning", "Wifi"])

if __name__ == '__main__':
    unittest.main()
