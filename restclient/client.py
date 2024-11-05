import requests
import uuid
from typing import Literal
from requests import (
    Session,
    JSONDecodeError,
    HTTPError,
)
from restclient.utilites import allure_attach
from restclient.configuration import Configuration
from logger import log


class RestClient:
    def __init__(self, configuration: Configuration):
        self.host = configuration.host
        self.set_headers(configuration.headers)
        self.disable_log = configuration.disable_log
        self.session = Session()
        self.log = log.bind(service='')

    def set_headers(self, headers: dict) -> None:
        if headers:
            self.session.headers.update(headers)

    def post(self, path, **kwargs) -> requests.Response:
        return self._send_request(method='POST', url=path, **kwargs)

    def get(self, path, **kwargs) -> requests.Response:
        return self._send_request(method='GET', url=path, **kwargs)

    def put(self, path, **kwargs) -> requests.Response:
        return self._send_request(method='PUT', url=path, **kwargs)

    def delete(self, path, **kwargs) -> requests.Response:
        return self._send_request(method='DELETE', url=path, **kwargs)

    @allure_attach
    def _send_request(self, method: Literal['PUT', 'DELETE', 'GET', 'POST'], url: str, **kwargs) -> requests.Response:
        log = self.log.bind(event_id=str(uuid.uuid4()))
        full_url = self.host + url

        if self.disable_log:
            rest_response = self.session.request(method=method, url=full_url, **kwargs)
            log.msg(
                event='Request',
                method=method,
                params=kwargs.get('params'),
                data=kwargs.get('data')
            )

            try:
                rest_response.raise_for_status()
            except HTTPError:
                raise HTTPError(rest_response.text, response=rest_response)
            return rest_response

        rest_response = self.session.request(method=method, url=full_url, **kwargs)
        log.msg(
            event='Response',
            status_code=rest_response.status_code,
            headers=rest_response.headers,
            json=self._get_json(rest_response)
        )
        try:
            rest_response.raise_for_status()
        except HTTPError:
            raise HTTPError(rest_response.text, response=rest_response)
        return rest_response

    @staticmethod
    def _get_json(rest_response):
        try:
            return rest_response.json()
        except JSONDecodeError:
            return {}
