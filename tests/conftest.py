from typing import Callable

import pytest
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmConfiguration
from helpers.account_helpers import AccountHelper
from services.dm_api_account import DmApiAccountFacade
from services.mailhog_api import MailhogApiFacade
from models.data_models.registration import Registration
from models.data_models.login_credentials import LoginCredentials


@pytest.fixture(scope="class")
def mailhog_api() -> MailhogApiFacade:
    mailhog_configuration = MailhogConfiguration(host="http://5.63.153.31:5025", disable_log=True)
    mail_api = MailhogApiFacade(mailhog_configuration)
    return mail_api


@pytest.fixture(scope="class")
def dm_api() -> DmApiAccountFacade:
    dm_configuration = DmConfiguration(host="http://5.63.153.31:5051", disable_log=True)
    dm_api = DmApiAccountFacade(dm_configuration)
    return dm_api


@pytest.fixture(scope="class")
def account_helper(dm_api, mailhog_api) -> AccountHelper:
    """
    Init not authorized  api helper class scope.
    :param dm_api: fixture init DmApiAccountFacade instance
    :param mailhog_api: fixture init MailhogApiFacade instance
    :return: AccountHelper
    """
    account_helper = AccountHelper(dm_account_api=dm_api, mailhog=mailhog_api)
    return account_helper


@pytest.fixture()
def auth_account_helper(mailhog_api) -> Callable:
    """
    Init authorized  api helper test function scope.
    :param mailhog_api: fixture init MailhogApiFacade instance
    :return: AccountHelper
    """

    def _make_auth_session(user: Registration) -> AccountHelper:
        dm_configuration = DmConfiguration(host="http://5.63.153.31:5051", disable_log=False)
        account = DmApiAccountFacade(dm_configuration)
        account_helper = AccountHelper(dm_account_api=account, mailhog=mailhog_api)
        account_helper.register_new_user(user)
        account_helper.auth_client(LoginCredentials(login=user.login, password=user.password))
        return account_helper

    return _make_auth_session
