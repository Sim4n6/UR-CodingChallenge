from flask import Blueprint, request
from flask import jsonify, make_response, abort

from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import SQLAlchemyError

from ur_cc_app import db
from ur_cc_app.models import (
    Shop,
    shop_schema,
)

# Blueprint Configuration
api_bp = Blueprint(
    "api_bp",
    __name__,
    url_prefix="/api/v1",
    template_folder="templates",
    static_folder="static",
)


@api_bp.route("/shops", methods=["GET"])
def listAllShops():

    limit = request.args.get("limit")
    sortByDistance = request.args.get("sortByDistance")
    print(f">>> Limit shops to : {limit} -- isSortedBy distance: {sortByDistance}")

    try:
        if limit != None:
            results = Shop.query.limit(limit)
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
    return "listAllPreferredShops"


@api_bp.route("/preferred_shops/<int:shopId>", methods=["POST"])
def addPreferredShop(shopId):
    return "addPreferredShop"


@api_bp.route("/preferred_shops/<int:shopId>", methods=["PUT"])
def updatePreferredShop(shopId):
    return "updatePreferredShop"


@api_bp.route("/preferred_shops/<int:shopId>", methods=["DELETE"])
def removePreferredShop(shopId):
    return "removePreferredShop"
