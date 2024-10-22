from restclient.client import Configuration
from dm_api_accounts.apis.account_api import AccountApi
from dm_api_accounts.apis.login_api import LoginApi


class DmApiAccountFacade:
    def __init__(self, configuration: Configuration):
        self.configuration = configuration
        self.login_api = LoginApi(self.configuration)
        self.account_api = AccountApi(self.configuration)
