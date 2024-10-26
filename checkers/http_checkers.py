from assertpy import (
    soft_assertions,
    assert_that,
)
import requests
from contextlib import contextmanager
from requests.exceptions import HTTPError


def get_values_by_field(response: dict, msg_field: str) -> list | str | None:
    for field, values in response["errors"].items():
        if field == msg_field:
            return values


@contextmanager
def check_status_code_http(expected_status_code: requests.codes.OK, field: str = None, message: str | list = None):
    try:
        yield
        if expected_status_code not in [requests.codes.OK, requests.codes.CREATED, requests.codes.NO_CONTENT]:
            raise AssertionError(f"Expected status code should be equal {expected_status_code}")
        if field and message:
            raise AssertionError(f"Message should be {message}, but request is successful")

    except HTTPError as err:
        with soft_assertions():
            assert_that(
                err.response.status_code, f"Expected code {err.response.status_code} not equal {expected_status_code}"
            ).is_equal_to(expected_status_code)

            if message:
                values = get_values_by_field(err.response.json(), field)
                assert_that(values, f"expected {message} not equal actual {values}").is_equal_to(message)
