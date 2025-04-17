# 📚 Library Management System (LMS)

A full-stack Library Management System built using Django and Django REST Framework. This project is organized into two apps — one for the frontend (`lmsapp`) and one for the backend API (`lmsapi`). It uses a MySQL database and includes setup for static files and templates.

---

## 🚀 Getting Started

## 🛠️ Setup Instructions

Follow these steps to get the project running locally:

### 1. Clone the Repository
```bash
git clone https://github.com/Gauri-Nishad/lms_task.git
cd lms_task

2. Create and Activate a Virtual Environment
python -m venv lmsenv
lmsenv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Create the Django Project and Apps
django-admin startproject lms .
python manage.py startapp lmsapp
python manage.py startapp lmsapi
5. Run the Development Server
python manage.py runserver
⚙️ MySQL Database Configuration
Make sure you have MySQL installed and a database named lmsdb created. Your settings.py should include the following:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lmsdb',
        'USER': 'root',
        'PASSWORD': 'gauri123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
📦 Installed Libraries
Here’s what’s included in the requirements.txt:
asgiref==3.8.1
certifi==2025.1.31
charset-normalizer==3.4.1
Django==5.2
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
idna==3.10
mysqlclient==2.2.7
PyJWT==2.9.0
requests==2.32.3
simplejwt==2.0.1
sqlparse==0.5.3
typing==3.7.4.3
tzdata==2025.2
urllib3==2.4.0

# in other way 👇
creATE A FOLDER NAME LMS

THen open this FOLDER In vscode

tHen open teRMINAL 

ruN THE COMMAND "python -m venv lmsenv" FOR CReATING VIRTUAL ENviRONMENT 

then actIVAte the VIRTUAl ENV by this command "lmsenv/scripts/activate"

THEN INSTALL DJANGO "PIP INSTALL DJANGO"
THEN CREATE PROJECT FOLDER NAMED "DJANGO-ADMIN STARTPROJECT LMS"
then PYTHON MANAGE.PY RUNSERVER  works 
then we have to create a two app first for frontend and second for backend

run command python manage.py startapp lmsapp then run python manage.py startapp lmsapi

then create static folder AND TEMPLATE FOLDER WHERE OUR APPS IS LOCATED MEANS IN MAIN FOLDER NAMED(lms)
I ALREDY DID SETTINGS OF STATIC  AND TEMPLATES 

HERE IS THE REQUIREMENT.TXT FILE FOR VERSION OF DJANGO AND OTHER LIBRARY
asgiref==3.8.1
certifi==2025.1.31
charset-normalizer==3.4.1
Django==5.2
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
idna==3.10
mysqlclient==2.2.7
PyJWT==2.9.0
requests==2.32.3
simplejwt==2.0.1
sqlparse==0.5.3
typing==3.7.4.3
tzdata==2025.2
urllib3==2.4.0

for my sql database 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'lmsdb',
        'USER': 'root',
        'PASSWORD': 'gauri123',
        'HOST': '127.0.0.1',   
        'PORT': '3306',
    }
}

 

