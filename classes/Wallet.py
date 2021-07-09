import uuid
import json
import hashlib


class Wallet:

    unique_id = ""
    balance = 0
    history = []

    def generate_unique_id(self):
        unique_id = uuid.uuid1()
        self.unique_id = unique_id

    def add_balance(self, amount):
        self.balance += amount

    def sub_balance(self, amount):
        self.balance -= amount

    def send():
        pass

    def save(self):
        with open("./content/wallets/{}.json".format(self.unique_id), "w+") as file:
            file.write(json.dumps(
                {"id": self.unique_id, "balance": self.balance}))
