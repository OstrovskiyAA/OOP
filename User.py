from dataclasses import dataclass
import pytest
from enum import Enum

USER_AGE=18

class Status(Enum):
    student = 'student'
    worker = 'worker'
@dataclass
class User:
    name:str
    age:int
    status:Status
    items:list[str]
    def is_adult(self):
        return self.age>=USER_AGE
    # def __init__(self, name, age, status, items):
    #     self.name = name
    #     self.age = age
    #     self.status = status
    #     self.items = items
    # def __eq__(self, other):
    #     return (self.name == other.name and
    #             self.age == other.age and
    #             self.status == other.status and
    #             self.items == other.items)

oleg = User(name='oleg', age=16, status=Status.student, items=['book', 'pen'])
oleg2 = User(name='oleg', age=16, status=Status.student, items=['book', 'pen'])
olga = User(name='olga', age=22, status=Status.worker, items=['book', 'pen', 'fruit'])
print(oleg.age)
def test_compare():
    if oleg == oleg2:
        print('Yes')
    else:
        print("No")