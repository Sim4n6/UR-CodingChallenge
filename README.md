# UR-CodingChallenge
A Python project for UnitedRemote Coding Challenge.

#### Description of files 

- dump-shops/shops/ *shops.bson* : a provided list of shops details in bson format.
- dump-shops/shops/ *import.py* : a py script to import the list of shops into a postgresql db. 
- *Pipfile* and *Pipfile.lock* : files of the pkg and virtual env management tool 'Pipenv'.
- *.pre-commit-config.yaml* : a pre-commit config file to let black execute at before each commit.
- *.gitignore* : a file to let git ignore some local files.   

#### Samples of commands

```
pipenv run black . # to code format using black, all source files located in "."
pipenv run pytest # check all tests in test_ files.
pipenv run pytest --cov=. # check a coverage source file located in "." using cov plugin.
pipenv run pre-commit run --all-files
```

```
# Set up of pre-commit and pre-push hooks once
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

#### References 

Based on <https://sourcery.ai/blog/python-best-practices/> and <https://docs.python-guide.org/writing/structure/>
