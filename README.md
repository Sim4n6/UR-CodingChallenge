# UR-CodingChallenge
A Python project for UnitedRemote Coding Challenge <https://github.com/hiddenfounders/web-coding-challenge>

## Files description

#### Import : 
- importing/ *shops.bson* : a provided list of shops details in bson format.
- *importing.py* : a py script to import the list of shops into a postgresql db for production environment or sqlite db for debug env.
- To run this file : ```python importing.py``` 

#### Config files :
- *Pipfile* and *Pipfile.lock* : files of the pkg and virtual env management tool 'Pipenv'.
- *.pre-commit-config.yaml* : a pre-commit config file to let black execute at before each commit.
- *.gitignore* : a file to let git ignore some local files.   

#### Webapp :
 - *run_app.py* : a py script to run the whole web app.
