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
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
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
    @api.response(400, 'Setter validation failed')
    def post(self):
        """Register a new place"""
        place_data = api.payload

        required_fields = ['title', 'description', 'price', 'latitude', 'longitude', 'owner_id']
        if not all(field in place_data for field in required_fields):
            return {'error': "Data: invalid input"}, 400
        
        owner_id = str(place_data.get('owner_id'))
        user = facade.get_user(owner_id)
        if not user:
            return {'error': "User does not exist"}, 400
        try:
            place_data['owner'] = user
            del place_data['owner_id']
            new_place = facade.create_place(place_data)

            return { 
                'id': str(new_place.id),
                'title': new_place.title, 
                'description': new_place.description, 
                'price': new_place.price, 
                'latitude': new_place.latitude, 
                'longitude': new_place.longtitude, 
                'owner_id': new_place.owner.id 
            }, 201
        except ValueError as error:
            return {'error': f"Setter validation failure: {str(error)}"}, 400


    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        return [{
            'id': str(place.id), 
            'title': place.title,  
            'latitude': place.latitude, 
            'longitude': place.longtitude, 
        } for place in facade.get_all_places()], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return{'error': 'Amenity not found'}, 404
        if not place.owner:
            return {'error': 'Owner information not found'}, 404

        amenities_list = []
        for amenity in place.amenities:
            amenities_list.append({
                'id': str(amenity.id),
                'name': amenity.name
            })
        
        return {
            'id': str(place.id),
            'title': place.title, 
            'description': place.description, 
            'latitude': place.latitude, 
            'longitude': place.longtitude,
            'owner': {
                'id': str(place.owner.id),
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name,
                'email': place.owner.email
            },
            'amenities': amenities_list
        }, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        place_data = api.payload
        required_fields = {'title', 'description', 'price'}

        if set(place_data.keys()) != required_fields:
            return {'error': 'Attributes are missing - Invalid data'}, 400
        if not facade.get_place(place_id):
            return {'error': 'Place not found'}, 404
        try:
            facade.update_place(place_id, place_data)
            return {'Message': 'Place updated successfully'}, 200
        except ValueError as error:
            return {'error': f"Setter validation failure: {str(error)}"}, 400
