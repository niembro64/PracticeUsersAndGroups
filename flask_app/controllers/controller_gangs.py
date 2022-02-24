from flask_app import app
from flask import render_template, request, redirect, flash, session
import re
from flask_app.models.user import User
from flask_app.models.gang import Gang
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/gangs")
def show_gangs():
    l = "show_gangs"
    Gang.p(l)
    # all_gangs = Gang.get_all_gangs()
    # return render_template("gangs.html", all_gangs = all_gangs)
    a = Gang.get_all_gangs_with_users()
    return render_template("gangs.html", a = a)

####################

@app.route("/gangs/fun_create_new", methods=["POST"])
def fun_create_new_gang():
    l = "fun_create_new_gang"
    Gang.p(l)
    data = {
        "name": request.form["name"]
    }
    Gang.save_gang(data)
    return redirect("/gangs")
