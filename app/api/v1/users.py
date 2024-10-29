from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'id': fields.String(readonly=True, description='The unique identifier of the user'),
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})

facade = HBnBFacade()

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201

    @api.response(200, 'Users list successfully retrieved')
    def get(self):
        all_users = facade.get_all_user()
        users_list = []
        for user in all_users:
            users_list.append({
                'id': str(user.id),
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            })
        return users_list, 200
        
@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User found')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get a specific user by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
            
        return {
            'id': str(user.id),
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        }, 200
        
    @api.expect(user_model)
    @api.response(200, 'User details updated successfully')
    @api.response(400, 'Invalid input data')
    @api.response(404, 'User not found')
    def put(self, user_id):
        user_data = api.payload

        updated_user = facade.update_user(user_id, user_data)
        if updated_user is None:
            return {'error': 'User not found.'}, 404
        return {
            'message': 'User updated successfully',
            'id': str(updated_user.id),
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email
        }, 200

     # Please use these Curl command tests for testing the endpoints for amenities.
     #  curl -X POST http://localhost:5000/api/v1/users/ -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}'
     #  curl -X GET "http://127.0.0.1:5000/api/v1/users/b98e3d06-3f9a-46a6-aabc-fe49f4641eb1" -H "Content-Type: application/json"
     #  curl -X GET "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json"
     #  curl -X PUT "http://127.0.0.1:5000/api/v1/users/b98e3d06-3f9a-46a6-aabc-fe49f4641eb1" -H "Content-Type: application/json" -d '{"first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com"}'
