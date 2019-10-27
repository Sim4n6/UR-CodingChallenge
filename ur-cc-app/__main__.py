from .main import main_routes
from .api import api_routes

from flask import Flask, render_template, make_response, request, jsonify, Blueprint
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder="templates", static_folder="static")
Bootstrap(app)

# register bluprints
app.register_blueprint(main_routes.main_bp)
app.register_blueprint(api_routes.api_bp)

# load env vars
from dotenv import load_dotenv

load_dotenv(verbose=True)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
