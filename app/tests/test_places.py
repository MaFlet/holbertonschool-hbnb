import unittest
from app.models.place import Place
from app.services.facade import HBnBFacade
from app import create_app

class TestPlaceAPI(unittest.TestCase):

    def setUp(self):
    
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.api = Api(self.app)
        self.api.add_namespace(api)

        self.client = self.app.test_client()

    
    def tearDown(self):
        """Cleaning up after each test"""
        if hasattr(self.place, 'places_repo'):
            self.facade.place_repo.clear()

    def test_create_place_success(self):
        response = self.client.post('/places/', json={
            'title': 'Cozy Cottage',
            'description': 'A lovely cottage in the woods.',
            'price': 100.0,
            'latitude': 34.0522,
            'longitude': -118.2437,
            'owner_id': '123',
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_create_place_user_not_found(self):
        response = self.client.post('/places/', json={
            'title': 'Cozy Cottage',
            'description': 'A lovely cottage in the woods.',
            'price': 100.0,
            'latitude': 34.0522,
            'longitude': -118.2437,
            'owner_id': 'nonexistent_user',
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_get_place_not_found(self):
        response = self.client.get('/places/999/')
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json)

    def test_get_place_success(self):
        response = self.client.get('/places/1/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('title', response.json)

    def test_update_place_success(self):
        response = self.client.put('/places/1/', json={
            'title': 'Updated Title',
            'description': 'Updated description.',
            'price': 150.0,
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Message', response.json)

    def test_update_place_not_found(self):
        response = self.client.put('/places/999/', json={
            'title': 'Updated Title',
            'description': 'Updated description.',
            'price': 150.0,
        })
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json)

    def test_get_all_places(self):
        response = self.client.get('/places/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

if __name__ == '__main__':
    unittest.main()
