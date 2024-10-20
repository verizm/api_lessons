import json
import random
import allure
import pytest
from http import HTTPStatus
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


@pytest.mark.usefixtures("init_api_clients")
class TestPutV1AccountEmail:

    @allure.title("Check login after change email")
    def test_post_v1_account_email(self):
        login = f"vera{random.randrange(1000)}"
        user = PostV1AccountsRequest(login=login, email=f"{login}@mail.ru", password="1234567889")
        login_data = PostV1LoginRequest(login=user.login, password=user.password)
        new_login = f"vera_new{random.randrange(1000)}"
        user_new_data = PostV1AccountsRequest(login=user.login, email=f"{new_login}@gmail.ru", password=user.password)


        # with allure.step("Change email data"):
        #     change_mail_resp = self.account_api.put_v1_account_email(user_new_data)
        #     assert change_mail_resp.status_code == HTTPStatus.OK, f"Error status code after change email: {change_mail_resp}"
        #
        # with allure.step("Login with new email"):
        #     login_response = self.login_api.post_v1_account_login(login_data)
        #     status_code = login_response.status_code
        #     assert status_code == HTTPStatus.FORBIDDEN, f"Error status code after login under not authorized user: {status_code}"
        #
        # with allure.step("Get new account token from mail"):
        #     mails = self.mailhog_api.get_api_v2_messages()
        #     token = get_token_by_login(user_new_data.login, mails.json())
        #
        # with allure.step("Authorize user with new email"):
        #     authorize_response = self.account_api.put_v1_account_token(token)
        #     status_code = authorize_response.status_code
        #     assert status_code == HTTPStatus.OK, f"Error status code after authorize user: {status_code}"
        #
        # with allure.step("Login under user after change email"):
        #     login_response = self.login_api.post_v1_account_login(login_data)
        #     status_code = login_response.status_code
        #     assert status_code == HTTPStatus.OK, f"Error status code after login user: {status_code}"
