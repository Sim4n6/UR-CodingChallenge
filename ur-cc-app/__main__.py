from .landing import landing_routes

from flask import Flask, render_template, make_response, request, jsonify, Blueprint

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(landing_routes.landing_bp)

# load env vars
from dotenv import load_dotenv

load_dotenv(verbose=True)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
