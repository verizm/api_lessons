import allure
from http import HTTPStatus
from checkers.http_checkers import check_status_code_http
from dm_api_accounts.models.login_credentials import LoginCredentials
from data.data_helpers.user_creator import UserCreator


@allure.suite("Check Put v1 account email endpoint")
@allure.sub_suite("Positive")
class TestPutV1AccountEmail:

    @allure.title("Authorize user after change email")
    def test_post_v1_account_email(self, account_helper):
        user = UserCreator.make_user()
        login_data = LoginCredentials(login=user.login, password=user.password)

        account_helper.register_new_user(user)
        account_helper.login_user(login_data)

        with allure.step("Change email data"):
            user.email = UserCreator.fake.generate_email()
            with check_status_code_http(HTTPStatus.OK):
                account_helper.dm_account_api.account_api.put_v1_account_email(user, validate_response=False)

        with allure.step("Login with new email without authorize"):
            with check_status_code_http(HTTPStatus.FORBIDDEN):
                account_helper.login_user(login_data)

        with allure.step("Check that user can authorize with new email"):
            token = account_helper.get_activation_token_by_login(user.login)
            with check_status_code_http(HTTPStatus.OK):
                account_helper.dm_account_api.account_api.put_v1_account_token(token, validate_response=False)
