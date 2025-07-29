# Django Resume Applicataion
This repo is an example of using Django with https://jsonresume.org/ in order to provide a web ready interface for individual resumes. 

## Running locally
- Clone the repository
- ```cd django-resume```
- Use the .env.example file to setup an .env file
- ```python manage.py migrate```
- ```python manage.py makesuperuser```
- Follow the instructions to setup an admin user
- ```python manage.py runserver```
- Navigate to /admin
- Create a new profile and resume. You can use the JSON file in resume/test_resources for an example
- Visit localhost:8000/ and localhost:8000/resume to see the site in action
