from typing import Callable
from pathlib import Path
from vyper import v
import pytest
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmConfiguration
from helpers.account_helpers import AccountHelper
from services.dm_api_account import DmApiAccountFacade
from services.mailhog_api import MailhogApiFacade
from dm_api_accounts.models.registration import Registration
from dm_api_accounts.models.login_credentials import LoginCredentials

options = (
    'service.dm_api_account',
    'service.mail_hog',
)


@pytest.fixture(scope="session", autouse=True)
def set_config(request):
    config = Path(__file__).joinpath("../../").joinpath("config")
    config_name = request.config.getoption("--env")
    v.set_config_name(config_name)
    v.add_config_path(config)
    v.read_in_config()
    for option in options:
        v.set(f"{option}", request.config.getoption(f"--{option}"))


def pytest_addoption(parser):
    parser.addoption("--env", action="store_true", default="stg", help="run stg")

    for option in options:
        parser.addoption(f"--{option}", action="store", default=None)


@pytest.fixture(scope="class")
def mailhog_api() -> MailhogApiFacade:
    mailhog_configuration = MailhogConfiguration(host=v.get('service.mail_hog'), disable_log=True)
    mail_api = MailhogApiFacade(mailhog_configuration)
    return mail_api


@pytest.fixture(scope="class")
def dm_api() -> DmApiAccountFacade:
    dm_configuration = DmConfiguration(host=v.get('service.dm_api_account'), disable_log=False)
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
        dm_configuration = DmConfiguration(host=v.get('service.dm_api_account'), disable_log=True)
        account = DmApiAccountFacade(dm_configuration)
        account_helper = AccountHelper(dm_account_api=account, mailhog=mailhog_api)
        account_helper.register_new_user(user)
        account_helper.auth_client(LoginCredentials(login=user.login, password=user.password))
        return account_helper

    return _make_auth_session
