# Django 5 Blog Application with Bootstrap

## Overview

This is blog application developed using Python with Django 5 for the backend and Bootstrap for the front end. The application allows users to create, view, update, and delete blog posts and comments. Bloggers can create accounts, write articles and even approve and disapprove unwanted comments (This functionality is under development).

![Screen Shot 2024-01-23 at 5 53 21 PM](https://github.com/hervenoubs/Django-5-Blog-Application-with-Bootstrap/assets/12233172/7a784916-b52b-4e6b-8402-05e4d2c3b815)

![Screen Shot 2024-01-23 at 5 54 40 PM](https://github.com/hervenoubs/Django-5-Blog-Application-with-Bootstrap/assets/12233172/c3e7d13c-debc-4725-b7a8-35b51598f978)


## Features for now

* Sign up, log in, and log out functionality.
* Secure user authentication and authorization mechanisms.
* Create, update, and delete blog posts for authenticated bloggers.
* Bloggers can manage all their respective posts.
* View a list of all blog posts with details such as title, author, publication date, and number of comments.
* Blog posts category listings on the top page for easy navigation.
* View each blog post individually.
* Comment section for readers to interact.
* Sidebar featuring blog categories and recent posts.
* Authenticated bloggers can publish and manage their posts.
* Visitors can subscribe to a custom database-driven newsletter for updates.
* Users can search for articles on the blog using a search feature.
* A simple about page
* Working contact page with a form submission feature for user inquiries.
* Utilize Bootstrap 5.3 for a responsive and mobile-friendly design.

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

accounts/: Django app for managing bloggers actions like add/view/delete posts and moderate their comments.
authentication/: Django app for signing up and logging in for bloggers.
blog/: Django app for the blog functionality.
static/: Contains static files (CSS, JavaScript).
templates/: Contains HTML templates.
venv/: Virtual environment directory.
manage.py: Django management script.
requirements.txt: List of Python dependencies.

Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
