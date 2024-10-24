## Objectives

By the end of this project, you should be able to:

- Set Up the Project Structure:

Organize the project into a modular architecture, following best practices for Python and Flask applications.
Create the necessary packages for the Presentation and Business Logic layers.

- Implement the Business Logic Layer:

Develop the core classes for the business logic, including User, Place, Review, and Amenity entities.
Implement relationships between entities and define how they interact within the application.
Implement the facade pattern to simplify communication between the Presentation and Business Logic layers.

- Build RESTful API Endpoints:

Implement the necessary API endpoints to handle CRUD operations for Users, Places, Reviews, and Amenities.
Use flask-restx to define and document the API, ensuring a clear and consistent structure.
Implement data serialization to return extended attributes for related objects. For example, when retrieving a Place, the API should include details such as the owner’s first_name, last_name, and relevant amenities.

- Test and Validate the API:

Ensure that each endpoint works correctly and handles edge cases appropriately.
Use tools like Postman or cURL to test your API endpoints.

1. The app/ directory contains the core application code.
1. The api/ subdirectory houses the API endpoints, organized by version (v1/).
1. The models/ subdirectory contains the business logic classes (e.g., user.py, place.py).
1. The services/ subdirectory is where the Facade pattern is implemented, managing the interaction between layers.
1. The persistence/ subdirectory is where the in-memory repository is implemented. This will later be replaced by a database-backed solution using SQL Alchemy.
1. run.py is the entry point for running the Flask application.
1. config.py will be used for configuring environment variables and application settings.
1. requirements.txt will list all the Python packages needed for the project.
1. README.md will contain a brief overview of the project.