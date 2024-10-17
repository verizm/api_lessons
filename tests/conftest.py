import pytest
import structlog
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmConfiguration
from dm_api_accounts.apis.account_api import AccountApi as AccountApi
from dm_api_accounts.apis.login_api import LoginApi
from api_mailhog.apis.mailhog_api import MailhogApi

structlog.configure(processors=[structlog.processors.JSONRenderer(indent=8, ensure_ascii=True)])


@pytest.fixture(scope="class")
def init_api_clients(request) -> None:
    """
    Init api handlers and set ti request.
    :param request:
    :return: None
    """
    mailhog_configuration = MailhogConfiguration(host="http://5.63.153.31:5025", disable_log=False)
    dm_configuration = DmConfiguration(host="http://5.63.153.31:5051", disable_log=False)

    setattr(request.cls, "account_api", AccountApi(configuration=dm_configuration))
    setattr(request.cls, "login_api", LoginApi(configuration=dm_configuration))
    setattr(request.cls, "mailhog_api", MailhogApi(configuration=mailhog_configuration))
