from flask import Blueprint, jsonify, request, g
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from ur_cc_app import db
from ur_cc_app import simple_geoip
from ur_cc_app.models import Shop, User, User_Shop, shop_schema
from ur_cc_app.auth import login_required

# Blueprint Configuration
api_bp = Blueprint(
    "api_bp",
    __name__,
    url_prefix="/api/v1",
    template_folder="templates",
    static_folder="static",
)


@api_bp.route("/shops", methods=["GET"])
@login_required
def listAllShops(sortByDistance=False):

    sortByDistance_arg = request.args.get("sortByDistance")

    try:
        if sortByDistance:
            results = Shop.query.all()
            geoip_data = simple_geoip.get_geoip_data()
            location = geoip_data.get("location")
            if location != None:
                user_lat = location.get("lat")
                user_lng = location.get("lng")
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
@login_required
def listAllPreferredShops():

    try:
        user = User.query.filter_by(email=g.user["email"]).one_or_none()
        if user:
            associations = User_Shop.query.filter_by(user_id=user.id).all()
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
@login_required
def addPreferredShop(shopId):
    try:
        user = User.query.filter_by(email=g.user["email"]).one_or_none()
        if user:
            shop = Shop.query.filter_by(id=shopId).first()
            # check whether User_Shop is already in association table
            association = (
                User_Shop.query.filter_by(user_id=user.id)
                .filter_by(shop_id=shop.id)
                .first()
            )
            if association is None:
                association = User_Shop(user_id=user.id, shop_id=shop.id)
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
@login_required
def removePreferredShop(shopId):
    try:
        user = User.query.filter_by(email=g.user["email"]).one_or_none()
        if user:
            shop = Shop.query.filter_by(id=shopId).first()
            # check whether User_Shop is already in association table
            association = (
                User_Shop.query.filter_by(user_id=user.id)
                .filter_by(shop_id=shop.id)
                .first()
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
