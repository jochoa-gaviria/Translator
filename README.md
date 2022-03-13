# Translator and blog app using Django

## Setting a virtual environment

* python3 -m venv env
* Activate virtual env - Ctrl+Shift+p and select the virtual env. or use "source env/bin/activate"
* python3 -m pip install --upgrade pip
* pip3 install django

## Diferent Comands

### To init a project

* django-admin startproject {name} .

### To run a project

* to run use - python3 manage.py runserver

### Migrations

* python3 manage.py migrate

#### After create models on app run should use

* python3 manage.py makemigrations
* python3 manage.py migrate

### Create a super user

* python3 manage.py createsuperuser

#### To create apps

* python3 manage.py startapp {name} to create an app


#### Install librarie to translations
* pip install googletrans