from flask import redirect, url_for

from ur_cc_app import create_app

app = create_app()


@app.route("/")
def index():
    return redirect(url_for("main_bp.index"))


if __name__ == "__main__":
    app.run()
