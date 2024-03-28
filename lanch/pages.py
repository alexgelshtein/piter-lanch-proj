from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/auth")
def auth():
    return render_template("pages/auth.html")

@bp.route("/admin")
def admin():
    return render_template("pages/admin.html")

#TODO:
@bp.route("/users/<int:ID>")
def users(ID):
    return render_template("pages/users.html")