import pytest
from dm_api_accounts.apis.account_api import AccountApi
from dm_api_accounts.apis.login_api import LoginApi
from api_mailhog.apis.mailhog_api import MailhogApi


@pytest.fixture(scope="class")
def init_api_clients(request) -> None:
    """
    Init api handlers and set ti request.
    :param request:
    :return: None
    """

    setattr(request.cls, "account_api", AccountApi(host="http://5.63.153.31:5051"))
    setattr(request.cls, "login_api", LoginApi(host="http://5.63.153.31:5051"))
    setattr(request.cls, "mailhog_api", MailhogApi(host="http://5.63.153.31:5025"))
