from datetime import datetime

from assertpy import assert_that
import allure
from hamcrest import (
    assert_that,
    has_property,
    has_properties,
    all_of,
    equal_to,
    starts_with,
    instance_of
)
from dm_api_accounts.models.registration import Registration
from dm_api_accounts.models.user_envelope import UserEnvelope


class PostV1AccountLogin:

    @classmethod
    def check_response_data(cls, response: UserEnvelope, user: Registration):
        with allure.step("Check user data"):
            assert_that(str(response.resource.registration), starts_with(datetime.now().strftime("%Y-%m-%d")))
            assert_that(
                response, all_of(
                    has_property("resource", has_property("login", starts_with("vera"))),
                    has_property("resource", has_property("roles", equal_to(["Guest", "Player"]))),
                    has_property("resource", has_property("registration", instance_of(datetime))),
                    has_property(
                        "resource",
                        has_property(
                            "rating",
                            has_properties(
                                {
                                    "enabled": equal_to(True),
                                    "quality": equal_to(0),
                                    "quantity": equal_to(0)
                                }
                            )
                        )
                    )
                )
            )
