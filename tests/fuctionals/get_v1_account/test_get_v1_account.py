from data.data_helpers.user_creator import UserCreator
from checkers.get_v1_account import GetV1Account


class TestGetV1Account:

    def test_get_v1_account(self, auth_account_helper):
        user = UserCreator.make_user()
        auth_account_helper = auth_account_helper(user)
        response = auth_account_helper.dm_account_api.account_api.get_v1_account(validate_response=True)
        GetV1Account.check_response_data(response, user)