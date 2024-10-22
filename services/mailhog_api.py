from restclient.client import Configuration
from api_mailhog.apis.mailhog_api import MailhogApi


class MailhogApiFacade:
    def __init__(self, configuration: Configuration):
        self.configuration = configuration
        self.mailhog_api = MailhogApi(self.configuration)
