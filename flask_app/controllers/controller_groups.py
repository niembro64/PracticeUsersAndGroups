from flask_app import app
from flask import render_template, request, redirect, flash, session
import re

from flask_app.models.user import User
from flask_app.models.group import Group

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)   

@app.route("/groups")
def show_groups():
    return render_template("groups.html")
