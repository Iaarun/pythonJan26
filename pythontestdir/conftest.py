import pytest

#@pytest.fixture(scope="session")
def preSessionSetup():
    print("Open Browser")
    yield
    print("Close Browser")

#@pytest.fixture(scope="module")
def premoduleSetup():
    print("This is the pre browser setup with module scope")

#@pytest.fixture(scope="function")
def firstPresetup():
    print("login before each testcase")
    yield
    print("logout after each testcase")

#@pytest.fixture(scope="class")
def preclassetup():
    print("This is the pre class setup")