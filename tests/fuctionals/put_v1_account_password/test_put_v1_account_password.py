import random
import allure
from models.data_models.registration import Registration
from models.data_models.change_password import ChangePassword
from models.data_models.reset_password import ResetPassword


class TestPutV1AccountPassword:

    def test_put_v1_account_password(self, auth_account_helper):
        login = f"vera{random.randrange(1000)}"
        user = Registration(login=login, email=f"{login}@mail.ru", password="1234567889")
        new_pass_data = ChangePassword(login=login, token="", old_password=user.password, new_password="12341111")
        reset_pass_data = ResetPassword(login=user.login, email=user.email)

        auth_account_helper = auth_account_helper(user)
        auth_account_helper.auth_client(user)
        response = auth_account_helper.change_password(reset_pass_data, new_pass_data)

        with allure.step("Check password changed succesfully"):
            assert response.status_code == 200, f"Incorrect status code after change password {response.status_code}"

        with allure.step("Check that user authorized with new password"):
            user.password = new_pass_data.new_password
            response = auth_account_helper.auth_client(user)
            assert response.status_code == 200, f"Incorrect status code auth user {response.status_code}"
