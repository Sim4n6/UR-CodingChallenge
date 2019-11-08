from flask import Blueprint, request, abort
from flask import render_template

from ..api import api_routes

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp",
    __name__,
    url_prefix="/main",
    template_folder="templates",
    static_folder="static",
)


@main_bp.route("/")
@main_bp.route("/index")
def index():
    """ Index view function """
    return render_template("index.html", title="Index web page")


@main_bp.route("/nearby", methods=["GET"])
def nearby():
    """Nearby shops view function."""

    # get all shops
    response = api_routes.listAllShops(limit=10, sortByDistance=1)
    all_shops = response[0].get_json()

    # get all preferred shops
    response = api_routes.listAllPreferredShops(sortByDistance=1)
    all_preferred_shops = response[0].get_json()

    # keep only those shops that are not in preferred shops
    the_shops = [shop for shop in all_shops if shop not in all_preferred_shops]

    return render_template("nearby.html", title="Nearby shops", all_shops=the_shops)


@main_bp.route("/preferred", methods=["GET"])
def preferred():
    """Preferred shops view function."""

    response = api_routes.listAllPreferredShops(sortByDistance=1)
    all_preferred_shops = response[0].get_json()
    return render_template(
        "preferred.html",
        title="Preferred shops",
        all_preferred_shops=all_preferred_shops,
    )
