import random
import allure
from http import HTTPStatus
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest
from models.api_models.api_login_models.post_v1_login_models import PostV1LoginRequest


class TestPutV1AccountEmail:

    @allure.title("Check login after change email")
    def test_post_v1_account_email(self, account_helper):
        login = f"vera{random.randrange(1000)}"
        user = PostV1AccountsRequest(login=login, email=f"{login}@mail.ru", password="1234567889")
        login_data = PostV1LoginRequest(login=user.login, password=user.password)
        new_login = f"vera_new{random.randrange(1000)}"
        user_new_data = PostV1AccountsRequest(login=user.login, email=f"{new_login}@gmail.ru", password=user.password)

        account_helper.register_new_user(user)
        account_helper.login_user(login_data)

        with allure.step("Change email data"):
            change_mail_resp = account_helper.dm_account_api.account_api.put_v1_account_email(user_new_data)
            assert change_mail_resp.status_code == HTTPStatus.OK, f"Error status code after change email: {change_mail_resp}"

        with allure.step("Login with new email without authorize"):
            login_response = account_helper.login_user(login_data)
            status_code = login_response.status_code
            assert status_code == HTTPStatus.FORBIDDEN, f"Error status code after login under not authorized user: {status_code}"

        with allure.step("Authorize user with new email"):
            token = account_helper.get_activation_token_by_login(new_login)
            login_response = account_helper.dm_account_api.account_api.put_v1_account_token(token)
            assert login_response.status_code == HTTPStatus.OK, f"Error status code after new authorize: {login_response.status_code}"
