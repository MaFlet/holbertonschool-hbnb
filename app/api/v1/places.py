from uuid import UUID
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

review_model = api.model('Review', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner of the place'),
    'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities'),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

facade = HBnBFacade()

def validate_uuid(uuid_string):
    """Validate UUID format for ID's"""
    try:
        uuid_obj = UUID(uuid_string, version=4)
        return str(uuid_obj)
    except (ValueError, AttributeError, TypeError):
        print(f"Invalid UUID format: {uuid_string}")
        return None

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(400, 'Setter validation failed')
    def post(self):
        """Register a new place"""
        place_data = api.payload
        print(f"Receiving place data: {place_data}")
        
        required_fields = ['title', 'description', 'price', 'latitude', 'longitude', 'owner_id']
        if not all(field in place_data for field in required_fields):
            missing_fields = [field for field in required_fields if field not in place_data]
            print(f"Missing fields: {missing_fields}")
            return {'error': "Data: invalid input"}, 400
        
        owner_id = place_data.get('owner_id')
        valid_uuid = validate_uuid(owner_id) # validate owner_id format
        if not valid_uuid:
            return {'error': "Invalid owner ID format"}, 400
        
        user = facade.get_user(valid_uuid)
        print(f"Looking up user with ID: {valid_uuid}")
        if not user:
            print(f"User not found with ID: {valid_uuid}")
            return {'error': "User does not exist"}, 400
        
        try:
            place_data['price'] = float(place_data['price'])
            place_data['latitude'] = float(place_data['latitude'])
            place_data['longitude'] = float(place_data['longitude'])

            place_data['owner'] = user
            del place_data['owner_id']

            new_place = facade.create_place(place_data)
        
            result = { 
                'id': str(new_place.id),
                'title': new_place.title, 
                'description': new_place.description, 
                'price': new_place.price, 
                'latitude': new_place.latitude, 
                'longitude': new_place.longitude, 
                'owner_id': str(new_place.owner.id) 
                }
            return result, 201
        
        except ValueError as error:
            print(f"Validation error: {str(error)}")
            return {'error': f"Setter validation failure: {str(error)}"}, 400
        except Exception as error:
            print(f"Unexpected error: {str(error)}")
            return {'error': "An unexpected error occurred"}, 500

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        try:
            places = facade.get_all_places()
            return [{
                'id': str(place.id), 
                'title': place.title,  
                'latitude': place.latitude, 
                'longitude': place.longitude, 
            } for place in places], 200
        except Exception as error:
            print(f"Error retrieving places: {str(error)}")
            return {'error': "Failed to retrieve places"}, 500

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        valid_uuid = validate_uuid(place_id)
        if not valid_uuid:
            return {'error': 'Invalid place ID format'}, 400
        
        try:
            place = facade.get_place(valid_uuid)
            if not place:
                return{'error': 'Place not found'}, 404
            if not place.owner:
                return {'error': 'Owner information not found'}, 404

            amenities_list = [{
                    'id': str(amenity.id),
                    'name': amenity.name
                } for amenity in place.amenities]
            
            return {
                'id': str(place.id),
                'title': place.title, 
                'description': place.description, 
                'latitude': place.latitude, 
                'longitude': place.longitude,
                'owner': {
                    'id': str(place.owner.id),
                    'first_name': place.owner.first_name,
                    'last_name': place.owner.last_name,
                    'email': place.owner.email
                },
                'amenities': amenities_list
            }, 200
        except Exception as error:
            print(f"Error retrieving place: {str(error)}")
            return {'error': 'Failed to retrieve place details'}, 500

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        valid_uuid = validate_uuid(place_id)
        if not valid_uuid:
            return {'error': 'Invalid place ID format'}, 400
        
        place_data = api.payload
        required_fields = {'title', 'description', 'price'}

        if set(place_data.keys()) != required_fields:
            return {'error': 'Attributes are missing - Invalid data'}, 400
        
        try:
            if not facade.get_place(place_id):
                return {'error': 'Place not found'}, 404
            
            place_data['price'] = float(place_data['price'])
            
            facade.update_place(valid_uuid, place_data)
            return {'message': 'Place updated successfully'}, 200
        except ValueError as error:
                return {'error': f"Setter validation failure: {str(error)}"}, 400
        except Exception as error:
            print(f"Error updating place: {str(error)}")
            return {'error': 'Failed to update place'}, 500

# Please use these Curl command tests for testing the endpoints for amenities.
 # curl -X POST "http://127.0.0.1:5000/api/v1/places/" -H "Content-Type: application/json" -d '{"title": "Wi-fi", "description": "A nice place to stay", "price": "100.0", "latitude": "37.37749", "longitude": "-122.4194", "owner_id": ""}'
 # curl -X GET "http://127.0.0.1:5000/api/v1/places/" -H "Content-Type: application/json"
 # curl -X GET "http://127.0.0.1:5000/api/v1/places/<place_id>"
 # curl -X PUT "http://127.0.0.1:5000/api/v1/places/<place_id>" -H "Content-Type: application/json" -d '{"title": "Luxury Condo", "description": "An upscale place to stay", "price": "200.0"}'