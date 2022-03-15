# first_django_web
### Steps
## SETUP
1. Create a VENV and install packages (pycharm simplifies this)
2. pip3 install django - or pip3 install pack1 pack2 pack3... packn-1 packn
3. pip3 freeze -> command used for requirements.txt. pip3 freeze > requirements.txt
4. mkdir src -> like java projects, where we store all the code
5. type -> django-admin startproject myprojectname -> creates the django project

## FIRST STUFF
1. manage.py -> orchestrates the whole app
2. type -> python3 manage.py runserver -> starts the app
3. type -> python3 manage.py migrate (gets rid of configuration warnings and enables security settings)
4. type -> python3 manage.py createsuperuser 