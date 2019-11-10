# UR-CodingChallenge
A Python project for UnitedRemote Coding Challenge <https://github.com/hiddenfounders/web-coding-challenge>

## Files description

#### Importing : 
- importing/ *shops.bson* : a provided list of shops details in bson format.
- *importing.py* : a py script to import the list of shops into a postgresql db for production environment or sqlite db for debug env.
- To run this file : ```python importing.py``` 

#### Config files :
- *Pipfile* and *Pipfile.lock* : files of the pkg and virtual env management tool 'Pipenv'.
- *.pre-commit-config.yaml* : a pre-commit config file to let black execute at before each commit.
- *.gitignore* : a file to let git ignore some local files.   

#### Webapp :
 - *run_app.py* : a py script to run the whole web app.
 - api/ blueprint 
 - auth/ blueprint
 - errors/ curstom errors handling blueprint
 - main/  main implemented functionnalities blueprint.
 - static/ static files including favicon, a simple JS file and CSS file.
 - templates/ common template such as layout.html
 - __init__.py
 - config.py 
 - models.py : models goes here.
