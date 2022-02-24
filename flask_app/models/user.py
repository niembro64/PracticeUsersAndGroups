from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import gang
from flask import flash
import re

class User:
    def __init__(self, data):
        self.id = data["id"]

        self.name = data["name"]
        self.email = data["email"]
        self.password = data["password"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_users(cls):
        l = "get_all_users"
        User.p(l)
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_and_gangs').query_db(query)
        all_users = []
        for row in results:
            one_user = cls(row)
            all_users.append(one_user)
        return all_users

    @classmethod
    def save_user(cls, data):
        l = "save_user"
        User.p(l)
        query = "INSERT INTO users (name, email, password, created_at, updated_at) VALUES (%(name)s, %(email)s, %(password)s, NOW(), NOW());"
        new_id = connectToMySQL("users_and_gangs").query_db(query, data)
        return new_id

    ##########################

    @staticmethod
    def p(l):
        print("------------------------------------------------")
        print(f"------------------------ {l}")
        print("------------------------------------------------")
