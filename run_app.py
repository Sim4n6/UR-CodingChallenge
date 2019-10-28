import os

from dotenv import load_dotenv
from flask import Blueprint, Flask, jsonify, make_response, render_template, request

from ur_cc_app import create_app

app = create_app()

# load env vars
load_dotenv(verbose=True)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
