from flask import Flask, render_template, make_response, request, jsonify, Blueprint

import os
from ur_cc_app import create_app

app = create_app()

# from ur_cc_app.models import Shop


# load env vars
from dotenv import load_dotenv

load_dotenv(verbose=True)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
