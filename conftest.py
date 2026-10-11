import pytest

from clients.user_client import UserClient


@pytest.fixture(scope="session")
def user_client():
    return UserClient()
