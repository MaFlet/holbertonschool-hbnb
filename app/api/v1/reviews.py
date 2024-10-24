from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

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

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        try:
            review_data = api.payload

            if not 1 <= review_data['rating'] <=5:
                return {'error': 'Rating must be between 1 and 5'}, 400
            
            new_review = facade.create_review(review_data)

            return {
                'id': str(new_review.id), 
                'text': new_review.text, 
                'rating': new_review.rating, 
                'user_id': str(new_review.user_id), 
                'place_id': str(new_review.place_id)
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'Internal server error'}, 500

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        try:
            reviews = facade.get_all_reviews()
            return [{
                'id': str(review.id), 
                'text': review.text,  
                'rating': review.rating, 
                'user_id': str(review.user_id),
                'place_id': str(review.place_id) 
            } for review in reviews], 200
        except Exception as e:
            return {'error': 'Internal server error'}, 500

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        try:
            review = facade.get_review(review_id)
            if not review:
                return{'error': 'Review not found'}, 404
            
            return {
                'id': str(review.id),
                'text': review.text, 
                'rating': review.rating, 
                'user_id': str(review.user_id), 
                'place_id': str(review.place_id),
            }, 200
        except Exception as e:
            return {'error': 'Internal server error', e}, 500
    
    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        try:
            review_data = api.payload

            if 'rating' in review_data and not 1 <= review_data['rating'] <=5:
                return {'error': 'Rating must be between 1 to 5'}, 400
            
            updated_review = facade.update_review(review_id, review_data)
            if not updated_review:
                return {'error': 'Review not found'}, 404
            return {
                'id': str(updated_review.id),
                'text': updated_review.text, 
                'rating': updated_review.rating, 
                'user_id': str(updated_review.user_id), 
                'place_id': str(updated_review.place_id),
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'Internal server error', e}, 500
        
    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        try:
            result = facade.delete_review(review_id)
            if not result:
                return {'error': 'Review not found'}, 404
            return {'message': 'Review deleted successfully'}, 200
        except Exception as e:
            return {'error': 'Internal server error'}, 500

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        try:
            place = facade.get_place(place_id)
            if not place:
                return {'error': 'Place not found'}, 404
            
            reviews = facade.get_reviews_by_place(place_id)
            return [{
                'id': str(review.id),
                'text': review.text, 
                'rating': review.rating, 
                'user_id': str(review.user_id), 
                'place_id': str(review.place_id),
            } for review in reviews], 200
        except Exception as e:
            return {'error': 'Internal server error', e}, 500
