import requests
from requests import Response


def test_delete_user():
    user_id = 5
    url = f'https://reqres.in/api/users/{user_id}'

    new_user: Response = requests.delete(url=url)

    assert new_user.status_code == 204
