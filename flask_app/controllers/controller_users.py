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
    return render_template("users.html")

####################

@app.route("/users/fun_create_new", methods=["POST"])
def fun_create_new_user():
    l = "fun_create_new_user"
    User.p(l)
    data = {
        "user_name": request.form["user_name"],
        "email": request.form["email"],
        "password": request.form["password"]
    }
    User.p("after data")
    user_id = User.save_user(data)
    return redirect("/users", user_id = user_id)
