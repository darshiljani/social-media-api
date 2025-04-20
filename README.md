# Social Media API

The social media API is a RESTful API set designed for a text-based dummy social media platform.

## Features

- User Registration / Login
- Posting content on feed
- Likes and comments on posts
- Error handling for invalid post or user retrieval

## Requirements

- Python 3.x
- [Django](https://docs.djangoproject.com/en/5.2/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django CORS Headers](https://pypi.org/project/django-cors-headers/)
- [Django Filter](https://django-filter.readthedocs.io/en/stable/)

## Setup

1. Clone the repository

`git clone https://github.com/darshiljani/social-media-api`

2. Setup virtual environment

- Create the environment  
   `virtualenv venv` (If virtualenv is installed)  
   `python -m venv venv` (If virtualenv is not installed)

- Activate the environment  
   `./venv/Scripts/activate` (If using Windows)  
   `source venv/bin/activate` (If using Linux)

3. Install the dependencies

`pip install -r requirements/local.txt`

4. Set up database credentials as environment variables

- Create a new file called .env in the project root folder
- Copy contents from .env.example into .env
- Replace the following values with actual credentials

```bash
DB_NAME=<db_name>
DB_USER=<db_user>
DB_PWD=<db_password>
```

5. Move into project folder

`cd server`

6. Create an admin user

`python manage.py createsuperuser`

7. Start the development server

`python manage.py runserver`

8. Access the API

`http://localhost:8000`

## Testing

The APIs can be tested using the Postman collection located at
[**Social Media API.postman_collection.json**](https://github.com/darshiljani/social-media-api/blob/master/README.md)
