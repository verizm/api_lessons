import allure
import requests
from restclient.client import RestClient


class MailhogApi(RestClient):

    @allure.step("Get emails")
    def get_api_v2_messages(self) -> requests.Response:
        """
        Get users emails.
        :param limit: count of mails in response
        :return: requests.Response
        """

        response = self.get(path="/api/v2/messages", params={"limit": 50})
        return response
