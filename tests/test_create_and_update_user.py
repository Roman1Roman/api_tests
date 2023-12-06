import jsonschema
import requests
from requests import Response

from utils.load_schema import load_schema


def test_create_and_update_same_user():
    """creating new user"""
    url_create = 'https://reqres.in/api/users'
    user_name = 'krasav4ik'
    user_job = 'tester'
    json_user_create = {
        "name": user_name,
        "job": user_job
    }
    schema_create = load_schema('../tests/schemas/response_created_user.json')

    new_user: Response = requests.post(url=url_create, json=json_user_create)

    assert new_user.status_code == 201
    assert new_user.json()['name'] == user_name
    assert new_user.json()['job'] == user_job
    jsonschema.validate(new_user.json(), schema_create)

    id_user = new_user.json()['id']

    """updating created user"""

    url_update = f'https://reqres.in/api/users/{id_user}'
    user_new_name = 'emo_is_cool'
    user_new_job = 'I like crying'
    json_user_update = {
        "name": user_new_name,
        "job": user_new_job
    }
    schema_update = load_schema('../tests/schemas/response_update_user.json')

    update_user: Response = requests.put(url=url_update, json=json_user_update)

    assert update_user.status_code == 200
    assert update_user.json()['name'] == user_new_name
    assert update_user.json()['job'] == user_new_job
    jsonschema.validate(update_user.json(), schema_update)
