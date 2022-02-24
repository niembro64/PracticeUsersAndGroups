from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash
import re

class Gang:
    def __init__(self, data):
        if "gang_id" in data:
            self.id = data["gang_id"]
        else:
            self.id = data["id"]

        if "gang_name" in data:
            self.name = data["gang_name"]
        else:
            self.name = data["name"]

        if "gang_created_at" in data:
            self.created_at = data["gang_created_at"]
        else:
            self.created_at = data["created_at"]

        if "gang_updated_at" in data:
            data["gang_updated_at"]
        else:
            self.updated_at = data["updated_at"]

    @classmethod
    def get_all_gangs_with_users(cls):
        l = "get_all_gangs_with_users"
        Gang.p(l)
        query = "SELECT users.id as user_id, users.name as user_name, gangs.id as gang_id, gangs.name as gang_id, users.email as email, users.password as password FROM gangs LEFT JOIN membership on membership.gang_id = gangs.id LEFT JOIN users on users.id = membership.user_id;"
        results = connectToMySQL('users_and_gangs').query_db(query)
        a = []
        for i in results:
            if not Gang(i) in a:
                g  = Gang(i)
                g.u.append(user.Users(i))
            else:
                g.u.append(user.Users(i))
            a.append(g)
        print(a)
        return a

    @classmethod
    def get_all_gangs(cls):
        l = "get_all_gangs"
        Gang.p(l)
        query = "SELECT * FROM gangs;"
        results = connectToMySQL('users_and_gangs').query_db(query)
        all_gangs = []
        for row in results:
            one_gang = cls(row)
            all_gangs.append(one_gang)
        return all_gangs

    @classmethod
    def save_gang(cls, data):
        l = "save_gang"
        Gang.p(l)
        query = "INSERT INTO gangs (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        new_id = connectToMySQL("users_and_gangs").query_db(query, data)
        return new_id

    ##########################

    @staticmethod
    def p(l):
        print("------------------------------------------------")
        print(f"------------------------ {l}")
        print("------------------------------------------------")
