from flask import Blueprint, jsonify, request
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from ur_cc_app import db
from ur_cc_app import simple_geoip
from ur_cc_app.models import Shop, User, User_Shop, shop_schema

# Blueprint Configuration
api_bp = Blueprint(
    "api_bp",
    __name__,
    url_prefix="/api/v1",
    template_folder="templates",
    static_folder="static",
)


@api_bp.route("/shops", methods=["GET"])
def listAllShops(sortByDistance=False):

    sortByDistance_arg = request.args.get("sortByDistance")

    try:
        if sortByDistance:
            geoip_data = simple_geoip.get_geoip_data()
            user_lat = geoip_data.get("location").get("lat")
            user_lng = geoip_data.get("location").get("lng")
            results = Shop.query.all()
            results.sort(key=lambda x: x.haversine(user_lat, user_lng))
        else:
            results = Shop.query.all()

        if results != None:
            return jsonify(shop_schema.dump(results)), 200
        else:
            return jsonify({"description": "Bad request."}), 400

    except OperationalError as e:
        return jsonify({"description": "Wraps a DB-API OperationalError."}), 500
    except SQLAlchemyError as e:
        return jsonify({"description": "SQLAlchemy Error ..."}), 500


@api_bp.route("/shops/<int:shopId>", methods=["POST"])
def addShop(shopId):
    return "addShop"


@api_bp.route("/shops/<int:shopId>", methods=["PUT"])
def updateShop(shopId):
    return "updateShop"


@api_bp.route("/preferred_shops", methods=["GET"])
def listAllPreferredShops():

    try:

        associations = User_Shop.query.filter_by(user_id=9).all()
        results = [
            Shop.query.filter_by(id=association.shop_id).first()
            for association in associations
        ]

        if results != None:
            return jsonify(shop_schema.dump(results)), 200
        else:
            return jsonify({"description": "Bad request."}), 400

    except OperationalError as e:
        return jsonify({"description": "Wraps a DB-API OperationalError."}), 500
    except SQLAlchemyError as e:
        return jsonify({"description": "SQLAlchemy Error ..."}), 500


@api_bp.route("/preferred_shops/<int:shopId>", methods=["POST"])
def addPreferredShop(shopId):
    try:
        shop = Shop.query.filter_by(id=shopId).first()
        # check whether User_Shop is already in association table
        association = (
            User_Shop.query.filter_by(user_id=9).filter_by(shop_id=shop.id).first()
        )
        if association is None:
            association = User_Shop(user_id=9, shop_id=shop.id)
            db.session.add(association)
            db.session.commit()
            return jsonify({"description": "Created."}), 201
        else:
            return jsonify({"description": "No response."}), 204

    except OperationalError as e:
        return jsonify({"description": "Wraps a DB-API OperationalError."}), 500
    except SQLAlchemyError as e:
        return jsonify({"description": "SQLAlchemy Error ..."}), 500


@api_bp.route("/preferred_shops/<int:shopId>", methods=["PUT"])
def updatePreferredShop(shopId):
    return "updatePreferredShop"


@api_bp.route("/preferred_shops/<int:shopId>", methods=["DELETE"])
def removePreferredShop(shopId):
    try:
        shop = Shop.query.filter_by(id=shopId).first()
        # check whether User_Shop is already in association table
        association = (
            User_Shop.query.filter_by(user_id=9).filter_by(shop_id=shop.id).first()
        )
        if association is not None:
            db.session.delete(association)
            db.session.commit()
            return jsonify({"description": "Deleted."}), 200
        else:
            return jsonify({"description": "No response."}), 204

    except OperationalError as e:
        return jsonify({"description": "Wraps a DB-API OperationalError."}), 500
    except SQLAlchemyError as e:
        return jsonify({"description": "SQLAlchemy Error ..."}), 500
