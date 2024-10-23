import random
import allure
from hamcrest import (
    assert_that, has_property, has_properties, all_of,  equal_to, has_length
)
from models.data_models.registration import Registration


class TestGetV1Account:

    def test_get_v1_account(self, auth_account_helper):
        login = f"vera{random.randrange(4000, 5000)}"
        user = Registration(login=login, email=f"{login}@mail.ru", password="1234567889")

        auth_account_helper = auth_account_helper(user)
        response = auth_account_helper.dm_account_api.account_api.get_v1_account(validate_response=True)
        with allure.step("Check user data"):
            assert_that(response, all_of(
                    has_property("resource", has_property("login", equal_to(login))),
                    has_property("resource", has_property("settings", has_property("color_schema", equal_to("Modern")))),
                    has_property("resource", has_property("info", has_length(0))),
                    has_property("resource", has_property("roles", equal_to(["Guest", "Player"]))),
                    has_property("resource", has_properties("settings", has_property("paging", has_properties(
                                                {
                                                    "posts_per_page": equal_to(10),
                                                    "comments_per_page": equal_to(10),
                                                    "topics_per_page": equal_to(10),
                                                    "messages_per_page": equal_to(10),
                                                    "entities_per_page": equal_to(10)
                                                }
                                            )
                                        )
                                    )
                                ),
                    has_property("resource", has_property("rating", has_properties(
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

