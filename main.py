import uuid
import json
import hashlib


from classes.Wallet import Wallet

if __name__ == '__main__':

    s = Wallet()

    s.add_balance(50)
    print(s.balance)
    s.sub_balance(10)
    print(s.balance)
    s.generate_unique_id()
    print(s.unique_id)
    s.save()
