# UR-CodingChallenge
A Python project for UnitedRemote Coding Challenge.

## Description of files 

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

#### Samples of commands

```
pipenv run black . # to code format using black, all source files located in "."
```

```
# Set up of pre-commit and pre-push hooks once
pipenv run pre-commit install -t pre-commit
```