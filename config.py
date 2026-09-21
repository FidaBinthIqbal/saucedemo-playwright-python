import os

BASE_URL = os.getenv(
    "SAUCEDEMO_BASE_URL",
    "https://www.saucedemo.com/"
)

STANDARD_USERNAME = os.getenv(
    "SAUCEDEMO_USERNAME",
    "standard_user"
)

STANDARD_PASSWORD = os.getenv(
    "SAUCEDEMO_PASSWORD",
    "secret_sauce"
)

LOCKED_USERNAME = os.getenv(
    "SAUCEDEMO_LOCKED_USERNAME",
    "locked_out_user"
)

INVALID_PASSWORD = os.getenv(
    "SAUCEDEMO_INVALID_PASSWORD",
    "wrong_password"
)