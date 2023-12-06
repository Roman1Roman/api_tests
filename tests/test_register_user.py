import jsonschema
import requests
from requests import Response

from utils.load_schema import load_schema


def test_register_user():
    url = 'https://reqres.in/api/register'
    user_email = 'eve.holt@reqres.in'
    user_password = 'pistol'
    json_user = {
        "email": user_email,
        "password": user_password
    }
    schema = load_schema('../tests/schemas/response_register_user_success.json')

    new_user: Response = requests.post(url=url, json=json_user)

    assert new_user.status_code == 200
    jsonschema.validate(new_user.json(), schema)

def test_register_user_400():
    url = 'https://reqres.in/api/register'
    user_email = 'ya@upadu.com'
    json_user = {
        "email": user_email
    }
    schema = load_schema('../tests/schemas/response_register_user_unsuccesful.json')

    new_user: Response = requests.post(url=url, json=json_user)

    assert new_user.status_code == 400
    jsonschema.validate(new_user.json(), schema)