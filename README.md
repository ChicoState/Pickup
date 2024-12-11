# Pickup

## About

### This is an app to provide students a place to plan sports, video games, or board games on the spot. Similiar to pickup basketball, no experience is required and everyone is welcome to join as long as there is enough room at that location.

## Running and Maintenance 

### To Run to test: 
install python, then run `source ./venv/bin/activate` then `python -m pip install -r requirements.txt` then `python mysite/manage.py runserver`

### Create Superuser
to make an admin user, follow the test run steps and instead of running `python mysite/manage.py runserver`, run `python mysite/manage.py createsuperuser` then follow the creation steps and notify other team members of the new superuser

### To Run with docker:
install python and docker, then use `docker compose up`


Both routes will host the site at localhost:8000

### To Stop docker:
Run `docker compose down`

### To update python requirements 
`python -m pip freeze > requirements.txt` while inside of venv

### Page template locations
`mysite/Pickup/templates` contains all web pages
pages are written in Django html with VUE

* `base.html` is the base html page applied to all other pages
* `index.html` is the landing page 
* `registration/login.html` is the login page
* `registration/register.html` is the registration page


### Page Styles
`mysite/Pickup/static/css` contains all css files