from flask import Blueprint
from flask import current_app as app
from flask import jsonify, make_response

from ur_cc_app import db
from ur_cc_app.models import Shops

# Blueprint Configuration
api_bp = Blueprint(
    "api_bp",
    __name__,
    url_prefix="/api",
    template_folder="templates",
    static_folder="static",
)


@api_bp.route("/shops", methods=["GET"])
def listAllShops():
    results = Shops.query.all()
    if results != None:
        print(results)
    return "listAllShops"


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
