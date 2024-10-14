import requests


class MailhogApi:
    def __init__(self, host, email=None):
        self.host = host
        self.email = email

    def get_api_v2_messages(self, limit: int = 50) -> requests.Response:
        """
        Get users emails.
        :param limit: count of mails in response
        :return: requests.Response
        """
        params = {"limit": limit}

        response = requests.get(url=f"{self.host}/api/v2/messages", params=params)
        return response
