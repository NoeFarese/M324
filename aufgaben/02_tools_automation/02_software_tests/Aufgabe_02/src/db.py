from pymongo import MongoClient
from src.models import User


class Db:
    def __init__(self, connection_string: str, db_name="testdb"):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.collection = self.db["users"]

    def set_user(self, user: User):
        self.collection.insert_one(user.to_dict())

    def get_user(self) -> User:
        data = self.collection.find_one()
        return User.from_dict(data)
