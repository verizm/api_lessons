from datetime import datetime

from assertpy import assert_that
import allure
from hamcrest import (
    assert_that,
    has_property,
    has_properties,
    all_of,
    equal_to,
    has_length,
    starts_with
)
from dm_api_accounts.models.registration import Registration
from dm_api_accounts.models.user_details_envelope import UserDetailsEnvelope


class GetV1Account:

    @classmethod
    def check_response_data(cls, response: UserDetailsEnvelope, user: Registration):
        with allure.step("Check user data"):
            assert_that(str(response.resource.registration), starts_with(datetime.now().strftime("%Y-%m-%d")))
            assert_that(
                response, all_of(
                    has_property("resource", has_property("login", equal_to(user.login))),
                    has_property("resource", has_property("settings", has_property("color_schema", equal_to("Modern")))),
                    has_property("resource", has_property("info", has_length(0))),
                    has_property("resource", has_property("roles", equal_to(["Guest", "Player"]))), has_property(
                        "resource",
                        has_properties(
                            "settings", has_property(
                                "paging", has_properties(
                                    {"posts_per_page": equal_to(10), "comments_per_page": equal_to(10),
                                        "topics_per_page": equal_to(10),
                                        "messages_per_page": equal_to(10), "entities_per_page": equal_to(10)}
                                )
                                )
                            )
                        ), has_property(
                        "resource",
                        has_property(
                            "rating",
                            has_properties({"enabled": equal_to(True), "quality": equal_to(0), "quantity": equal_to(0)})
                            )
                        )
                    )
                )
