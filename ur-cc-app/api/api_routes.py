from flask import Blueprint, make_response, jsonify
from flask import current_app as app

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
