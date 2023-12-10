import pytest
from dotenv import load_dotenv


@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()