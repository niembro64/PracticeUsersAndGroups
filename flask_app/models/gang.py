from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Gang:
    def __init__(self, data):
        self.id = data["id"]

        self.name = data["name"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

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
