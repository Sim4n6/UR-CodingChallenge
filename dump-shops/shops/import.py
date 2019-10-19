import os

import bson
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# load env variables
from dotenv import load_dotenv
load_dotenv()

# create an engine to handle connection to DB on the remote server
engine = create_engine(os.getenv("DB_URI"), echo=True)
conn = engine.connect()

# create table
conn.execute(""" CREATE TABLE IF NOT EXISTS "shops" ( 
	"id" SERIAL NOT NULL PRIMARY KEY,
	"picture" VARCHAR(200) NOT NULL,
	"name" VARCHAR(100) NOT NULL,
	"email" VARCHAR(100) NOT NULL,
	"city" VARCHAR(100) NOT NULL,
	"coord_type" VARCHAR(50) NOT NULL,
	"coordinate_lat" REAL NOT NULL,
	"coordinate_long" REAL NOT NULL
); """)

# bson to python dict with a generator
f = open('shops.bson','rb')
for i, entity in enumerate(bson.decode_file_iter(f)):
    print(i, "---------")
    picture = entity.get("picture")
    name =  entity.get("name")
    print( picture, name) 

    email = entity.get("email")
    city = entity.get("city")
    print( email, city )
    
    coord_type = entity.get("location").get("type")
    coordinate_lat = entity.get("location").get("coordinates")[0]
    coordinate_long = entity.get("location").get("coordinates")[1]
    print( coord_type, coordinate_lat, coordinate_long)

    # check if shop is duplicate 
    result = conn.execute(text("""SELECT id FROM shops WHERE name = :name AND email = :email AND coordinate_lat = :coordinate_lat AND coordinate_long = :coordinate_long; """), {"name":name, "email":email, "coordinate_lat":coordinate_lat, "coordinate_long":coordinate_long}).fetchone()
    if result == None :
        trans = conn.begin()
        conn.execute(text(""" INSERT INTO shops (picture, name, email, city, coord_type, coordinate_lat, coordinate_long) VALUES (:picture, :name, :email, :city, :coord_type, :coordinate_lat, :coordinate_long)"""), {"picture":picture, "name":name, "email":email, "city":city, "coord_type":coord_type, "coordinate_lat":coordinate_lat, "coordinate_long":coordinate_long})
        trans.commit()
    else:
        print("----------------> found a duplicate shop.")

f.close()
conn.close()