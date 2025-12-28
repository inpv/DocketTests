from faker import Faker
from config import config
import requests
import json

# This class is responsible for generating new user objects. As well as registering the API tokens which are used in
# the tests.

class Generate(object):
    def __init__(self):
        fake = Faker()

        self.user = {
            "Username": fake.name().split(' ', 1)[0],
            "Email Address": fake.email(),
            "Password": fake.word(),
            "Todo": fake.word()
        }

    def get_user(self):
        new_user = self.user
        return new_user

    def get_token(self):
        r = requests.post(config.SERVER + '/api/Register/',
                          json={'Username': self.user["Username"], 'Email Address': self.user["Email Address"],
                                'Password': self.user["Password"]})
        r.raise_for_status()
        try:
            response_json = r.json()
            token = response_json.get("token")
            if token:
                return token
            else:
                return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON: {r.text}")
            return None




