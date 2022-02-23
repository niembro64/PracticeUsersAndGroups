from flask_app import app
from flask import render_template, request, redirect, flash, session

from flask_app.models.user import User
from flask_app.models.group import Group


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/")
def index_to_users():
    print_location = "index_to_users"
    User.print_location(print_location)
    return redirect("/users")


@app.route("/users")
def show_users():
    print_location = "show_users"
    User.print_location(print_location)
    return render_template("users.html")

####################


@app.route("/users/fun_create_new", methods=["POST"])
def fun_create_new():
    print_location = "fun_create_new"
    User.print_location(print_location)
    data = {
        "user_name": request.form["user_name"],
        "email": request.form["email"],
        "password": request.form["password"]
    }
    User.print_location("after data")
    user_id = User.save_user(data)
    return user_id
