import os

import bson
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker


from ur_cc_app import config

# get the configs based on the current environment
current_config = vars(config.config_choices[os.getenv("FLASK_CONFIG") or "Development"])
print(current_config)

basedir = os.path.abspath(
    os.path.dirname(__file__)
)  # TODO switch to pathlib becuz it is recommened.

# create an engine to handle connection to DB on the remote server
engine = create_engine(current_config.get("SQLALCHEMY_DATABASE_URI"), echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Declare mapping
Base = declarative_base()

# model
class Shop(Base):
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True)
    picture = Column(String(200))
    name = Column(String(100))
    email = Column(String(100))
    city = Column(String(100))
    coord_type = Column(String(50))
    coordinate_lat = Column(Numeric)
    coordinate_long = Column(Numeric)

    def __repr__(self):
        return f"<Shop {name}>"


# create schema
Base.metadata.create_all(engine)

# bson to python dict with a generator
f = open(os.path.join(basedir, "importing", "shops.bson"), "rb")
for i, entity in enumerate(bson.decode_file_iter(f)):
    print(i, "---------")
    picture = entity.get("picture")
    name = entity.get("name")
    print(picture, name)

    email = entity.get("email")
    city = entity.get("city")
    print(email, city)

    coord_type = entity.get("location").get("type")
    coordinate_lat = entity.get("location").get("coordinates")[0]
    coordinate_long = entity.get("location").get("coordinates")[1]
    print(coord_type, coordinate_lat, coordinate_long)

    # check if shop is duplicate
    result = (
        session.query(Shop)
        .filter(Shop.name == name)
        .filter(Shop.email == email)
        .one_or_none()
    )
    if result == None:
        shop = Shop(
            picture=picture,
            name=name,
            email=email,
            city=city,
            coord_type=coord_type,
            coordinate_lat=coordinate_lat,
            coordinate_long=coordinate_long,
        )
        session.add(shop)
        session.commit()
    else:
        print(f"----------------> found a duplicate shop : {result}")

f.close()
session.close()
