import requests
from restclient.client import RestClient


class MailhogApi(RestClient):

    def get_api_v2_messages(self, limit: int = 50) -> requests.Response:
        """
        Get users emails.
        :param limit: count of mails in response
        :return: requests.Response
        """
        params = {"limit": limit}

        response = self.get(path="/api/v2/messages", params=params)
        return response
