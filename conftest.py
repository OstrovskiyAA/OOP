import csv
import pytest
from User import User, USER_AGE, Status


@pytest.fixture
def users() -> list[User]:
    with open("users.csv") as file:
        users = list(csv.DictReader(file, delimiter=";"))
    return [
        User(name=user['name'],
            age=int(user['age']),
            status=Status(user['status']),
            items=user['items'])
        for user in users
        ]


@pytest.fixture
def workers(users) -> list[User]:
    workers = []
    for user in users:
        if user.status == Status.worker:
            workers.append(user)
    return workers


# workers = [user for user in users if user["status"] == "worker"] - генератор списков
# {key: value for key, value in some_dict.items() if pass}

