import requests
from models.api_models.api_login_models.post_v1_login_models import PostV1LoginRequest
from restclient.client import RestClient


class LoginApi(RestClient):

    def post_v1_account_login(self, json_data: PostV1LoginRequest) -> requests.Response:
        """
        Authenticate via credentials.
        :param json_data:
        :return: status code
        """
        response = self.post(path="/v1/account/login", json=json_data.model_dump())

        return response
