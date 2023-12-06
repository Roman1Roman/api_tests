import jsonschema
import requests
from requests import Response

from utils.load_schema import load_schema


def test_create_user():
    url = 'https://reqres.in/api/users/'
    user_name = 'krasav4ik'
    user_job = 'tester'
    json_user = {
        "name": user_name,
        "job": user_job
    }
    schema = load_schema('../tests/schemas/response_created_user.json')

    new_user: Response = requests.post(url=url, json=json_user)

    assert new_user.status_code == 201
    assert new_user.json()['name'] == user_name
    assert new_user.json()['job'] == user_job
    jsonschema.validate(new_user.json(), schema)

