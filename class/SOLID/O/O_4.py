"""
4. Создание тестовых данных — средняя

Создай генераторы тестовых пользователей:

обычного пользователя;
администратора;
заблокированного пользователя.

Каждый генератор должен возвращать словарь с тестовыми данными пользователя.

Создай класс TestDataFactory, который получает генератор и создаёт данные через общий метод.

Добавление нового типа пользователя не должно требовать изменения TestDataFactory.
"""

from abc import ABC, abstractmethod


class Generator(ABC):
    @abstractmethod
    def generate(self):
        pass


class GenerateUser(Generator):
    def generate(self) -> dict:
        user = {
            "name": "Алексей",
            "age": 25,
            "is_blocked": False,  # False — не блокирован, True — блокирован
            "role": "user"  # "user" — обычный, "admin" — администратор
        }
        return user


class GeneratorUserBlock(Generator):
    def generate(self) -> dict:
        user = {
            "name": "Валерий",
            "age": 26,
            "is_blocked": True,  # False — не блокирован, True — блокирован
            "role": "user"  # "user" — обычный, "admin" — администратор
        }
        return user


class GeneratorAdmin(Generator):
    def generate(self) -> dict:
        admin = {
            "name": "Анатолий",
            "age": 40,
            "is_blocked": False,  # False — не блокирован, True — блокирован
            "role": "admin"  # "user" — обычный, "admin" — администратор
        }

        return admin


class TestDataFactory:

    def generate_user(self, gen: Generator) -> dict:
        return gen.generate()


user = GenerateUser()
admin = GeneratorAdmin()
user_block = GeneratorUserBlock()

gen_test_users = TestDataFactory()

print(gen_test_users.generate_user(admin))
print(gen_test_users.generate_user(user))
print(gen_test_users.generate_user(user_block))
