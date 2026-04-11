import pytest

@pytest.fixture(params= [("admin","admin123"),("user1","user123"),("user2","user123")])
def login_data(request):
    print( request.param)

@pytest.mark.sanity
@pytest.mark.login
def test_login(login_data):
    print("This is login test")

@pytest.mark.sanity
def test_logout():
    print("This is logout test")

@pytest.mark.regression
@pytest.mark.sanity

def test_registration():
    print("This is registration test")