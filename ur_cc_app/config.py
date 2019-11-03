import os

# the directory of config.py file
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ENV = "production"


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join( basedir , 'db.sqlite3' )}"
    SECRET_KEY = "#l9@)_DF6451FS165"
    ENV = "development"


config_choices = {"Production": ProdConfig, "Development": DevConfig}
