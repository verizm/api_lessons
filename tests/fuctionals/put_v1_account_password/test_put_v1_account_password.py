import allure
from dm_api_accounts.models.change_password import ChangePassword
from dm_api_accounts.models.reset_password import ResetPassword
from data.data_helpers.user_creator import UserCreator
from checkers.http_checkers import check_status_code_http


@allure.suite("Check Put v1 account password endpoint")
@allure.sub_suite("Positive")
class TestPutV1AccountPassword:

    @allure.title("Authorize user after change password")
    def test_put_v1_account_password(self, auth_account_helper):
        user = UserCreator.make_user()
        new_pass_data = ChangePassword(
            login=user.login,
            token="",
            old_password=user.password,
            new_password=UserCreator.fake.generate_password()
        )
        reset_pass_data = ResetPassword(login=user.login, email=user.email)

        auth_account_helper = auth_account_helper(user)
        auth_account_helper.auth_client(user)

        with check_status_code_http(200):
            auth_account_helper.change_password(reset_pass_data, new_pass_data)

        with allure.step("Check that user authorized with new password"):
            user.password = new_pass_data.new_password
            with check_status_code_http(200):
                auth_account_helper.auth_client(user)
