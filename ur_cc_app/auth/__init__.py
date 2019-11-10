from functools import wraps

from flask import g, redirect, url_for


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        if g.user:
            return f(*args, **kwds)
        return redirect(url_for("auth_bp.login"))

    return wrapper


# def is_logged_in():
#     if g.user:
#         return True
#     return False
