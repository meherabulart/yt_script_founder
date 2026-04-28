from flask import Blueprint, request, redirect
from models import db, User

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["POST"])
def signup():
    u = User(username=request.form["username"],
             password=request.form["password"])
    db.session.add(u)
    db.session.commit()
    return redirect("/")