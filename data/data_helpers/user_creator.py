from data.data_generator import DataGenerator
from dm_api_accounts.models.registration import Registration


class UserCreator:

    fake = DataGenerator()

    @staticmethod
    def make_user() -> Registration:

        return Registration(
            login=UserCreator.fake.generate_login(),
            email=UserCreator.fake.generate_email(),
            password=UserCreator.fake.generate_password()
        )
