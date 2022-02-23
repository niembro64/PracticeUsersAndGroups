from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re


class Group:
    def __init__(self, data):
        self.id = data["id"]

        self.name = data["name"]
        self.type = data["type"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        