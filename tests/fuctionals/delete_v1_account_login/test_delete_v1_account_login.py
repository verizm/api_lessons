import allure
from data.data_helpers.user_creator import UserCreator
from checkers.http_checkers import check_status_code_http


@allure.suite("Check Delete v1 login endpoint")
@allure.sub_suite("Positive")
class TestDeleteV1AccountLogin:
    @allure.title("Logout user")
    def test_delete_v1_account_login(self, auth_account_helper):
        user = UserCreator.make_user()
        auth_account_helper = auth_account_helper(user)

        with check_status_code_http(204):
            auth_account_helper.dm_account_api.login_api.delete_v1_account_login()
