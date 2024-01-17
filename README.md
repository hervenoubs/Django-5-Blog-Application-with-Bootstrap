# Django 5 Blog Application with Bootstrap

## Overview

This is blog application developed using Python with Django 5 for the backend and Bootstrap for the front end. The application allows users to create, view, update, and delete blog posts and comments. Bloggers can create accounts, write articles and even approve and disapprove unwanted comments (This functionality is under development).

![Screen Shot 2024-01-11 at 12 37 26 AM](https://github.com/hervenoubs/Django-5-Blog-Application-with-Bootstrap/assets/12233172/28342151-10a0-42cc-a22c-7856eb02fc85)


## Features for now

- User authentication (Sign up, Log in, Log out)
- Create, update, and delete blog posts
- View a list of all blog posts with their number of comments
- View each blog post including the comment section and sidebar at the right to see blog categories and recent posts
- Blog posts category listings 
- Users can subscribe to the blog 
- Users can search blog articles 
- About page
- Contact Us page with its active contact form
- Responsive design using Bootstrap

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- Django 5.x
- Bootstrap 5.x (included via CDN in the template)

## Getting Started

1. Clone the repository:

   ```bash
   git clone git@github.com:hervenoubs/Django-5-Blog-Application-with-Bootstrap.git
   cd blog-app-in-django
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py createsuperuser
5. python manage.py runserver

Project Structure

authentication/: Django app for signing up and logging in for bloggers.
blog/: Django app for the blog functionality.
static/: Contains static files (CSS, JavaScript).
templates/: Contains HTML templates.
venv/: Virtual environment directory.
manage.py: Django management script.
requirements.txt: List of Python dependencies.

Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
