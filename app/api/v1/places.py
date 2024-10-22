from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner details'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

facade = HBnBFacade()

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        place_data = api.payload
        new_place = facade.create_place(place_data)
        return { 
            'title': new_place.title, 
            'description': new_place.description, 
            'price': new_place.price, 
            'latitude': new_place.latitude, 
            'longitude': new_place.longtitude, 
            'owner_id': new_place.owner_id, 
        }

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        place_list = facade.get_all_places()
        return [{
            'title': place.title, 
            'description': place.description, 
            'price': place.price, 
            'latitude': place.latitude, 
            'longitude': place.longtitude, 
            'owner_id': place.owner_id, 
        } for place in place_list], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if place is None:
            return{'error': 'Amenity not found'}, 404
        owner = facade.get_user(place.owner_id)
        if owner is None:
            return {'error': 'Owner information not found'}, 404
        amenities = facade.get_place_amenities(place_id)
        return {
            'place_id': str(place.place_id),
            'title': place.title, 
            'description': place.description, 
            'price': place.price, 
            'latitude': place.latitude, 
            'longitude': place.longtitude,
            'owner': {
                'owner_id': str(place.owner_id),
                'first_name': place.first_name,
                'last_name': place.last_name,
                'email': place.email
            },
            'amenities': [
                {
                    'id': place.id,
                    'name': place.name
                },
                {
                    'id': place.id,
                    'name': place.id
                }
            ]
        }

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        place_data = api.payload
        updated_place = facade.update_place(place_id, place_data)
        if updated_place is None:
            return {'error': 'Amenity not found.'}, 404
        return {
            'message': 'Place updated successfully',
            'id': str(updated_place.id),
            'name': updated_place.name
        }, 200
