import jsonschema
import requests

from utils.load_schema import load_schema


def test_get_user():
    user_id = 5
    url = f'https://reqres.in/api/unknown/{user_id}'

    schema = load_schema('../tests/schemas/response_get_single_user.json')

    user_info = requests.get(url=url)

    assert user_info.status_code == 200
    jsonschema.validate(user_info.json(), schema)

def test_get_user_404():
    user_id = 0
    url = f'https://reqres.in/api/unknown/{user_id}'

    user_info = requests.get(url=url)

    assert user_info.status_code == 404
