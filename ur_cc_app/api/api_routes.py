from flask import Blueprint, request
from flask import jsonify, make_response, abort

from ur_cc_app import db
from ur_cc_app.models import (
    Shops,
    shop_schema,
)  # FIXME name of SHops --> Shop everywhere

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
    print(f" limit to : {limit} -- sorting {sortByDistance}")

    if limit != None:
        results = Shops.query.limit(limit)
    else:
        results = Shops.query.all()

    if results != None:
        return jsonify(shop_schema.dump(results)), 200
    else:
        abort(400)  # Bad request


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
