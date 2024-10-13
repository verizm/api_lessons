from dataclasses import dataclass
import json
import random
from dm_api_accounts.apis.account_api import AccountApi
from dm_api_accounts.apis.login_api import LoginApi
from api_mailhog.apis.mailhog_api import MailhogApi
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest
from models.api_models.api_login_models.post_v1_login_models import PostV1LoginRequest


def get_token_by_login(login: str, mails) -> str:
    """
    Get access token by user login.
     """
    for item in mails['items']:
        user_content = json.loads(item['Content']['Body'])
        if user_content["Login"] == login:
            token = user_content["ConfirmationLinkUrl"].split("/")[-1]
            return token
        else:
            raise Exception(f"Access token not found by login {login}")


class TestPostV1Accounts:

    def test_post_v1_account(self):
        account_api = AccountApi(host="http://5.63.153.31:5051")
        login_api = LoginApi(host="http://5.63.153.31:5051")
        mailhog_api = MailhogApi(host="http://5.63.153.31:5025")
        login = f"vera{random.randrange(1000)}"
        user = PostV1AccountsRequest(login=login, email=f"{login}@mail.ru", password="1234567889")

        register_response = account_api.post_v1_account(user)
        assert register_response == 201, f"Error status code after reqister user: {register_response}"

        mails = mailhog_api.get_api_v2_messages()
        token = get_token_by_login(user.login, mails)
        authorize_response = account_api.put_v1_account_token(token)
        assert authorize_response == 200, f"Error status code after authorize user: {authorize_response}"
        login_data = PostV1LoginRequest(login=user.login, password=user.password)
        login_response = login_api.post_v1_account_login(login_data)
        assert login_response == 200, f"Error status code after login user: {login_response}"
