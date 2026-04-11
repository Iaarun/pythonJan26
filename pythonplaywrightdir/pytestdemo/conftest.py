import pytest


@pytest.fixture(autouse=True)
def tc_setup():
    print("Launch Browser")
    print("Navigate to Login Page")
    yield
    print("Logout from the application")
    print("Close the browser")