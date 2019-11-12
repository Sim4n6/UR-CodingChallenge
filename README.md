# UR-CodingChallenge
A Python project for UnitedRemote Coding Challenge <https://github.com/hiddenfounders/web-coding-challenge>

## Check it out 

 ---> <https://ur-coding-challenge.herokuapp.com>

## How to use the web app 

 - You need first to choose your mode "Production" / "Development" / "Testing" and assign that value to the environment variable ```FLASK_CONFIG``` .
 - Corresponding to the chosen mode, check all env variables on Config.py (maybe u'll have to create an account on https://www.whoisxmlapi.com for API KEY)
 - run ``` python importing.py```  to import everything ( Shops/ Fake associations/ 02 fake user accounts ) to your db.
 - run the webapp using Gunicorn ``` gunicorn run_app:app```  or Flask integreted webserver ``` python run_app.py``` 

## Files description

#### Importing : 
- importing/ *shops.bson* : a provided list of shops details in bson format.
- *importing.py* : a py script to import the list of shops into a postgresql db for production environment or sqlite db for debug env.
- To run this file : ```python importing.py``` 

#### Webapp :
 - *run_app.py* : a py script to run the whole web app.
 
 ##### api 
 - *api/* : a blueprint for api side of the webapp.
 - *api/api_routes.py* : contains the api with view functions. Some routes are kept for future dev.
 - *api/openapi.json* : This file is optional, hence can be deleted, initially I was planning to use Connexion framework (on top of Flask) with Swagger editor. Than I discovered that the api is very simple : basically 04 routes. 
 
 ##### auth 
 - *auth/* : a blueprint for authentification functionnalities of the webapp such as registration and login (signup and signin).
 - *auth/templates* : contains two templates login.html and registration.html. Those templates are jinja2 enabled and inherits from ur_cc_app/templates/layout.html template.
 - *auth/auth_forms.py* : contains two forms for login and registration with the use of WTForms framework.
 - *auth/auth_routes.py* : login and registration routes are implemented here with their logic. It uses bcrypt module for hashing passwords. 
 
 ##### errors
  - *errors/* : a blueprint for curstom error handling with their templates
 
 ##### main 
 
  - *main/* : a blueprint for nearby and preferred functionnalities logic.
  - *main/templates* : contains three templates "index.html" for the landing page, "nearby.html" for nearby shops listing, and "preferred.html" for listing preferred shops.  
 
##### else

 - static/ static files including favicon, a simple JS file for like/dislike/remove clicking functionnalities and a CSS file to do some styling factorization.
 - templates/ common template such as layout.html from which all templates of the webpage inherits.
 - config.py : a way to organize the environment variables necessary for the functionning of the webapp. To choose the right mode Production/Testing/Development you need to set the environment variable FLASK_CONFIG before starting the app otherwise it will start on Development mode.
 - models.py : models that map to the relational database goes in this file. I use a basic use of Marshmallow module to make the models json enabled.
 - *Pipfile* and *Pipfile.lock* : files of the pkg and virtual env management tool 'Pipenv'.
 - *.pre-commit-config.yaml* : a pre-commit config file to let black execute at before each commit.
 - *.gitignore* : a file to let git ignore some local files.   