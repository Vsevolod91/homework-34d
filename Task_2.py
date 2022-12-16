import timeit
from functools import partial

class Person:
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email

class PersonTest:
    __slots__ = ("name", "address", "email")

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email

def get_set_delete(person):

    getattr(person, "name")
    getattr(person, "address")
    getattr(person, "email")

    delattr(person, "name")
    delattr(person, "address")
    delattr(person, "email")

    setattr(person, "name", "Ivan")
    setattr(person, "address", "123567 Pushkinskaya ul.")
    setattr(person, "email", "ivan@mail.ru")

def main():
    person = Person("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    person_test = PersonTest("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    old = min(timeit.repeat(partial(get_set_delete, person), number=1000000))
    new = min(timeit.repeat(partial(get_set_delete, person_test), number=1000000))
    print(f"Текущая реализация: {old}")
    print(f"Тестовая реализация: {new}")
    print(f"Улучшение производительности: {(old - new) / old:.2%}")


if __name__ == "__main__":
    main()