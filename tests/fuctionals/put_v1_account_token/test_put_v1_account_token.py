import random
import allure
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest


class TestPutV1AccountToken:

    @allure.title("Put access token")
    def test_put_v1_account_token(self, account_helper):
        login = f"vera{random.randrange(1000)}"
        user = PostV1AccountsRequest(login=login, email=f"{login}@mail.ru", password="1234567889")
        account_helper.dm_account_api.account_api.post_v1_account(user)
        token = account_helper.get_activation_token_by_login(login)
        account_helper.dm_account_api.account_api.put_v1_account_token(token)
