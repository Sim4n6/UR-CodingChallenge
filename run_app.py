import os

from flask import Blueprint, Flask, jsonify, make_response, render_template, request

from ur_cc_app import create_app

app = create_app()


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
