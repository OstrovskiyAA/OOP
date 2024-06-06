from User import User, USER_AGE


def test_workers_are_adult(workers):
    for worker in workers:
        assert worker.is_adult(), f"Worker {worker.name} is younger than 18"

#
# def user_is_adult(user:User):
#     return user.age >= USER_AGE