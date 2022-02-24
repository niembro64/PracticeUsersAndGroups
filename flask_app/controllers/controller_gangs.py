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
    return render_template("gangs.html")

####################

@app.route("/gangs/fun_create_new", methods=["POST"])
def fun_create_new_gang():
    l = "fun_create_new_gang"
    Gang.p(l)
    data = {
        "name": request.form["name"]
    }
    Gang.p("after data")
    gang_id = Gang.save_gang(data)
    return redirect("/gangs", gang_id = gang_id)
