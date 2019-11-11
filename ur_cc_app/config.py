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
    PROPAGATE_EXCEPTIONS = False
    GEOIPIFY_API_KEY = os.getenv("CONFIG_KEY_GEOIP")


# intermediate step toward production environment.
class TestConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join( basedir , 'db.sqlite3' )}"
    SECRET_KEY = "065dD4D684_#@@@"
    ENV = "production"
    PROPAGATE_EXCEPTIONS = False
    GEOIPIFY_API_KEY = "at_I86W4ISrof7Fe6J0hyENE484CFUsq"  # will be regenerated


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join( basedir , 'db.sqlite3' )}"
    SECRET_KEY = "#l9@)_DF6451FS165"
    ENV = "development"
    GEOIPIFY_API_KEY = "at_gEZIRbbXFSpa2smsmIUvTgi5MpJb1"  # will be regenerated


config_choices = {
    "Production": ProdConfig,
    "Testing": TestConfig,
    "Development": DevConfig,
}
