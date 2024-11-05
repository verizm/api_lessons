import allure

from checkers.http_checkers import check_status_code_http
from data.data_helpers.user_creator import UserCreator


@allure.suite("Check Put v1 account token endpoint")
@allure.sub_suite("Positive")
class TestPutV1AccountToken:

    @allure.title("Authorize user")
    def test_put_v1_account_token(self, account_helper):
        user = UserCreator.make_user()
        account_helper.dm_account_api.account_api.post_v1_account(user)
        token = account_helper.get_activation_token_by_login(user.login)
        with allure.step("Check that user authorized"):
            with check_status_code_http(200):
                account_helper.dm_account_api.account_api.put_v1_account_token(token)
