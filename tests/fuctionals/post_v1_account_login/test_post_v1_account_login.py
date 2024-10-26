import allure
from dm_api_accounts.models.login_credentials import LoginCredentials
from checkers.post_v1_account_login import PostV1AccountLogin
from data.data_helpers.user_creator import UserCreator


class TestPostV1AccountLogin:

    @allure.title("Check register user")
    def test_post_v1_account_login(self, account_helper):
        user = UserCreator.make_user()
        login_data = LoginCredentials(login=user.login, password=user.password)

        account_helper.register_new_user(user)
        with allure.step(f"Check login new user: {user}"):
            login_response = account_helper.login_user(login_data, validate_response=True)
            PostV1AccountLogin.check_response_data(login_response, user)

