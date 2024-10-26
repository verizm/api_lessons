from faker import Faker
from random import randrange
from datetime import datetime


class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    @staticmethod
    def generate_login() -> str:
        return f"vera_{datetime.now().strftime('%Y_%m_%d_%s')}_{randrange(0,10000)}"

    def generate_email(self) -> str:
        return f"{self.generate_login()}@mail.ru"

    def generate_password(self, length: int = 8) -> str:
        return self.fake.password(length=length, digits=True, special_chars=False)
