from typing import *


class User:

    def __init__(self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password


class Admin:

    def __init__(self, login, password):
        self.login = login
        self.password = password


@runtime_checkable
class Person(Protocol):
    name: str
    mail: str
    password: str


def lenUserList(objs: List[Person]):
    A = []
    for obj in objs:
        A.append(obj)
    print('Users =', len(A))


def showData(users):
    for user in users:
        if isinstance(user, Person):
            print(f"\nName = {user.name}\n"
                  f"Mail = {user.mail}\n"
                  f"Password = {user.password}\n")

        else:
            print("Користувач є адміністратором")


userList = []
userList.append(User("User1", "0000", "user1@gmail.com"))
userList.append(User("User2", "1234", "user2@gmail.com"))
userList.append(Admin("Admin", "root"))
# showData(userList)

lenUserList(userList)