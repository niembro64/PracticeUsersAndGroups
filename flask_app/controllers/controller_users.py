from lib2to3.refactor import get_all_fix_names
from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.user import User
from flask_app.models.gang import Gang
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index_to_users():
    l = "index_to_users"
    User.p(l)
    return redirect("/users")

@app.route("/users")
def show_users():
    l = "show_users"
    User.p(l)
    all_users = User.get_all_users()
    User.p(all_users)
    return render_template("users.html", all_users = all_users)

####################

@app.route("/users/fun_create_new", methods=["POST"])
def fun_create_new_user():
    l = "fun_create_new_user"
    User.p(l)
    data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "password": request.form["password"]
    }
    User.p(data)
    user_id = User.save_user(data)
    return redirect("/users")
