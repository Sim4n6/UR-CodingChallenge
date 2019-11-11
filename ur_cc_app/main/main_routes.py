from flask import Blueprint, render_template, request

from ur_cc_app.api.api_routes import listAllPreferredShops, listAllShops

from ur_cc_app.auth import login_required

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp",
    __name__,
    url_prefix="/main",
    template_folder="templates",
    static_folder="static",
)


@main_bp.route("/index")
def index():
    """ Index view function """
    return render_template("index.html", title="Index web page")


@main_bp.route("/nearby", methods=["GET"])
@login_required
def nearby():
    """Nearby shops view function."""

    # get all shops
    response = listAllShops(limit=None, sortByDistance=True)
    all_shops = response[0].get_json()

    # get all preferred shops
    response = listAllPreferredShops()
    all_preferred_shops = response[0].get_json()

    # keep only those shops that are not in preferred shops
    the_shops = [shop for shop in all_shops if shop not in all_preferred_shops]

    return render_template("nearby.html", title="Nearby shops", all_shops=the_shops)


@main_bp.route("/preferred", methods=["GET"])
@login_required
def preferred():
    """Preferred shops view function."""

    response = listAllPreferredShops(sortByDistance=1)
    all_preferred_shops = response[0].get_json()
    return render_template(
        "preferred.html",
        title="Preferred shops",
        all_preferred_shops=all_preferred_shops,
    )
