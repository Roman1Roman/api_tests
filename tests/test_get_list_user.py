import jsonschema
import requests

from utils.load_schema import load_schema


def test_get_list_users():
    number_of_page = 3
    url = f'https://reqres.in/api/users?page={number_of_page}'

    schema = load_schema('../tests/schemas/response_get_list_users.json')

    user_list = requests.get(url=url)

    assert user_list.status_code == 200
    assert user_list.json()['page'] == number_of_page
    jsonschema.validate(user_list.json(), schema)