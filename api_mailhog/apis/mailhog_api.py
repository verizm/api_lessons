import requests
import json


class MailhogApi:
    def __init__(self, host, email=None):
        self.host = host
        self.email = email

    def get_api_v2_messages(self, limit: int = 50):
        """
        Get users emails.
        :param login:
        :return:
        """
        params = {"limit": limit}

        response = requests.get(url=f"{self.host}/api/v2/messages", params=params)

        print(response.status_code)
        content = json.loads(response.content)
        return content
