import requests

BASE_URL = "http://127.0.0.1:8000"


def login(email, password):

    response = requests.post(

        f"{BASE_URL}/auth/login",

        data={

            "username": email,

            "password": password

        }

    )

    return response


def get_current_user(token):

    response = requests.get(

        f"{BASE_URL}/auth/me",

        headers={

            "Authorization": f"Bearer {token}"

        }

    )

    return response