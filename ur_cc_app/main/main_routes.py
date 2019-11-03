from flask import Blueprint, request, abort
from flask import render_template

from requests.exceptions import RequestException
import requests

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp",
    __name__,
    url_prefix="/main",
    template_folder="templates",
    static_folder="static",
)


@main_bp.route("/nearby", methods=["GET"])
def nearby():
    """Nearby shops view function."""

    try:
        all_shops = []
        # FIXME prepare an url independant from localhost
        payload = {"limit": 5, "sortByDistance": 1}
        r = requests.get("http://localhost:5000/api/v1/shops", params=payload)
        if r.status_code == 200:
            all_shops = r.json()
        else:
            abort(r.status_code, r.json().get("description"))

    except RequestException as e:
        abort(500, str(e))
    else:
        return render_template("nearby.html", title="Nearby shops", all_shops=all_shops)


@main_bp.route("/preferred", methods=["GET"])
def preferred():
    """Preferred shops view function."""
    return render_template("preferred.html", title="Preferred shops")
