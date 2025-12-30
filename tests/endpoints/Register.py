import requests
import json
from tests.config import config


class Register:
    def __init__(self):
        self.url = config.SERVER + '/api/Register/'

    def create_user(self, user):

        # A token is passed back by the server if the registration is a success
        r = requests.post(self.url,
                          json={'Username': user["Username"], 'Email Address': user["Email Address"],
                                'Password': user["Password"]})
        r.raise_for_status()
        try:
            response_json = r.json()
            token = response_json.get("token")
            if not token:
                return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON: {r.text}")
            return None

        # A request is then made to delete the user to reset the server back to its initial state
        result = requests.delete(config.SERVER + '/api/Users/', headers={'token': token}).text

        return result
